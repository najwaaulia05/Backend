import os
import mysql.connector
from flask import Flask, jsonify, request
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import datetime  # Untuk menangani objek timedelta jika ada

app = Flask(__name__)

# Konfigurasi koneksi ke Cloud SQL
db_config = {
    'host': '34.50.67.157',  # Ganti dengan IP Cloud SQL atau 'localhost' jika di dalam GAE
    'user': 'root',
    'password': 'Mampirsoloaja890#',
    'database': 'kulinerkitav2'
}

# Load model ML
model = load_model("model_ml.keras")

# Fungsi untuk menghitung jarak Haversine
def calculate_haversine(lat1, lon1, lat2, lon2):
    earth_radius = 6371  # Radius bumi dalam km
    delta_lat = np.radians(lat2 - lat1)
    delta_lon = np.radians(lon2 - lon1)
    a = np.sin(delta_lat / 2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(delta_lon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return earth_radius * c

# Fungsi untuk mengambil data restoran dari Cloud SQL
def fetch_data_from_db():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.id, p.name, p.address, p.phone_number, p.latitude, p.longitude, p.category_id, 
               p.categorize_weather, p.maps_url, p.min_price, p.max_price, p.kecamatan_id, p.eco_friendly,
               r.rating, r.reviews, o.opening_time, o.closing_time
        FROM places p
        INNER JOIN ratings r ON p.id = r.place_id
        INNER JOIN operatinghours o ON p.id = o.place_id
    """)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

@app.route("/predict", methods=["POST"])
def predict(): 
    try:
        # Mendapatkan data latitude dan longitude dari request JSON
        data = request.get_json()
        if not data or 'latitude' not in data or 'longitude' not in data:
            return jsonify({"error": "Missing latitude or longitude in request"}), 400

        current_lat = data['latitude']
        current_lon = data['longitude']

        # Ambil data restoran dari Cloud SQL
        df_all = fetch_data_from_db()

        # Hitung jarak menggunakan Haversine
        for row in df_all:
            row["computed_distance"] = calculate_haversine(current_lat, current_lon, row['latitude'], row['longitude'])

        # Hitung weighted rating
        C = np.mean([row['rating'] if row['rating'] is not None else 0 for row in df_all])
        M = np.median([row['reviews'] if row['reviews'] is not None else 0 for row in df_all])

        # Perhitungan weighted rating dengan pengecekan nilai None
        for row in df_all:
            rating = row['rating'] if row['rating'] is not None else 0
            reviews = row['reviews'] if row['reviews'] is not None else 0
            row['weighted_rating'] = ((reviews / (reviews + M)) * rating) + ((M / (reviews + M)) * C)

        # Ambil fitur untuk prediksi
        features = [(row['computed_distance'], row['weighted_rating']) for row in df_all]

        # Normalisasi data fitur
        scaler = MinMaxScaler()
        features_normalized = scaler.fit_transform(features)

        # Prediksi menggunakan model
        predictions = model.predict(features_normalized)

        # Menyusun hasil dengan data yang seragam sesuai format
        for i, row in enumerate(df_all):
            row['predicted_distance'] = predictions[i]

        # Sort hasil berdasarkan predicted_distance
        result = sorted(df_all, key=lambda x: x['predicted_distance'])

        # Menghapus duplikasi berdasarkan ID restoran
        seen = set()
        unique_results = []

        for row in result:
            if row['id'] not in seen:
                seen.add(row['id'])
                unique_results.append(row)

        # Menyusun top 10 rekomendasi tanpa duplikasi dengan urutan properti yang benar
        top_recommendation = [
            {
                "id": row["id"],
                "name": row["name"],
                "address": row["address"],
                "phone_number": row["phone_number"],
                "latitude": row["latitude"],
                "longitude": row["longitude"],
                "category_id": row["category_id"],
                "categorize_weather": row["categorize_weather"],
                "maps_url": row["maps_url"],
                "min_price": row["min_price"],
                "max_price": row["max_price"],
                "kecamatan_id": row["kecamatan_id"],
                "eco_friendly": row["eco_friendly"],
                "rating": "{:.2f}".format(row["rating"]),  # Format rating menjadi string dengan 2 angka desimal
                "reviews": row["reviews"],
                "operating_hours": {
                    "opening_time": str(row["opening_time"]),  # Pastikan waktu dalam format string
                    "closing_time": str(row["closing_time"])   # Pastikan waktu dalam format string
                }
            }
            for row in unique_results[:10]  # Ambil 10 rekomendasi teratas
        ]

        # Membuat dictionary dengan urutan yang benar
        response = {
            "success": "Prediksi berhasil",
            "data": top_recommendation
        }

        return jsonify(response), 200
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

if __name__ == "__main__":
    app.run(debug=True)
