# Menggunakan image Python 3.12 sebagai base image
FROM python:3.12-slim

# Set working directory di dalam kontainer
WORKDIR /app

# Menyalin file requirements.txt ke dalam kontainer
COPY requirements.txt .

# Menginstall dependencies yang ada di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh file dari project ke dalam kontainer
COPY . .

# Menjalankan aplikasi Flask
CMD ["python", "app.py"]

# Expose port 8080 untuk Cloud Run
EXPOSE 8080
