# 🍲 KulinerKita - Cloud Computing
## 🍴 KulinerKIta (Team C242-PS155) - CC Repository

**KulinerKita Cloud Computing Repository** for Bangkit Capstone Project. Building Scalable Cloud Infrastructure for a Culinary Platform with Serverless Functions and Cloud Databases.

## KulinerKita's Developer of Cloud Computing Bangkit Academy Capstone Team C242-PS155
|            Member           | Student ID |        Path        |                    Role                    |                                                       Contacts                                                      |
| :-------------------------: | :--------: | :----------------: | :----------------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| Dzaki Akmal Rabbani Alqadrie | C312B4KY1214  |  Cloud Computing  | Cloud Engineer |[dzakiakmal](https://github.com/dzakiakmal)|
| Fanes Arasadina          | C421B4KX1388 |  Cloud Computing  | Cloud Engineer | [fanesarasy](https://github.com/fanesarasy) |

**This is the Cloud Computing repository for the KulinerKita application.**  

---  

**KulinerKita** is a dynamic mobile app that helps users discover dining places such as restaurants, cafes, and street food. This section of the project focuses on the **Cloud Computing** aspect, which includes cloud infrastructure setup, database management, and server-side logic. Utilizing cloud services, it enhances the app's scalability, performance, and real-time features.

## Implementation Section:
- **Cloud Database Management**: Stores and manages data about dining places, categories, reviews, operating hours, and more.
- **APIs**: Enables communication between the mobile app and cloud resources, allowing for efficient search, filtering, and user interactions.
- **Scalability & Performance**: Uses cloud solutions to ensure the app can handle growing data and increasing numbers of users.

---

## Features

- **City and Subdistrict Search**: Filter restaurants by city or specific subdistrict.
- **Category-Based Search**: Find restaurants based on their category.
- **Eco-Friendly Options**: Search for restaurants that are environmentally friendly.
- **Weather Preferences**: Get recommendations for restaurants suitable for specific weather conditions.
- **Operating Hours**: Search restaurants open in the morning, afternoon, night, or operating 24 hours.
- **Ratings and Reviews**: Filter restaurants by minimum ratings and number of reviews.
- **Price Range**: Query restaurants within a specific price range.
- **Optimized Results**: Returns results with neatly formatted ratings and operating hours.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/kulinerkita/CC.git
   cd backend-v2
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up the database connection:
   - Create a `db.js` file in the project root with your database connection configuration.

4. Start the server:
   ```bash
   node server.js
   ```

5. Access the API at:
   ```
   http://localhost:3000
   ```

## API Endpoints

### `GET /restaurants/search`

Search for restaurants based on various filters.

#### Query Parameters

| Parameter      | Type    | Description                                         |
|----------------|---------|-----------------------------------------------------|
| `city`         | String  | Filter by city.                                    |
| `subdistrict`  | String  | Filter by subdistrict ID.                          |
| `ecoFriendly`  | Boolean | Filter by eco-friendly status.                     |
| `weather`      | String  | Filter by weather category.                        |
| `categoryId`   | Number  | Filter by restaurant category ID.                  |
| `openingHours` | String  | Filter by operating hours (e.g., `Morning`, `24 hours`). |
| `minRating`    | Number  | Filter by minimum rating.                          |
| `minReviews`   | Number  | Filter by minimum number of reviews.               |
| `minPrice`     | Number  | Filter by minimum price.                           |
| `maxPrice`     | Number  | Filter by maximum price.                           |

#### Example Request
```bash
GET https://kulinerkita.et.r.appspot.com/restaurants/search?categoryId=6
```

#### Example Response
```json
[
  {
        "id": 246,
        "name": "Selat Solo Tenda Biru - Dr. Wahidin",
        "address": "Jl. Dr. Wahidin No.26, Purwosari, Kec. Laweyan, Kota Surakarta, Jawa Tengah 57142",
        "phone_number": "082136659775",
        "latitude": -7.5686559,
        "longitude": 110.8052207,
        "category_id": 6,
        "categorize_weather": "Dingin",
        "maps_url": "https://www.google.com/maps/place/Selat+Solo+Tenda+Biru+-+Dr.+Wahidin/@-7.5686559,110.8052207,764m/data=!3m2!1e3!4b1!4m6!3m5!1s0x2e7a15d40a61c385:0x97027f5ac68485d3!8m2!3d-7.5686559!4d110.8052207!16s%2Fg%2F11b6zv3lhm?authuser=0&entry=ttu&g_ep=EgoyMDI0MTExOS4yIKXMDSoASAFQAw%3D%3D",
        "min_price": 25000,
        "max_price": 50000,
        "kecamatan_id": 1,
        "eco_friendly": 0,
        "rating": "4.60",
        "reviews": 7090,
        "operating_hours": {
            "opening_time": "08:00:00",
            "closing_time": "21:00:00"
        }
   }
]
```

## Project Structure

```
backend-v2/
├── db.js              # Database connection configuration
├── server.js          # Main application server
└── package.json       # Node.js dependencies and scripts
```

## Technologies Used

- **Node.js**: JavaScript runtime for building scalable applications.
- **Express**: Web framework for Node.js.
- **Cloud SQL (MySQL)**: Relational database management system.
- **Google App Engine**: Deploying the application and APIs automatically.
- **Cloud Run**: Deploying the machine learning models.
- **Google Cloud Storage**: For storing image and media data. 

---

## **Database Schema**

The database schema consists of several tables that are interrelated to manage restaurant data, including information on categories, locations, ratings, and operational hours. Below is a breakdown of each table and its relationships.

## 1. `places` Table
This table stores information about restaurants or dining places.

### Key Columns:
- **id**: Primary key of the table.
- **category_id**: Foreign key referencing the `categories` table (indicating the restaurant's category).
- **kecamatan_id**: Foreign key referencing the `kecamatan` table (indicating the location of the restaurant).

### Relationships:
- **One-to-Many** with `categories`: A category can be associated with many restaurants.
- **One-to-Many** with `kecamatan`: A kecamatan (district) can have many restaurants.
- **One-to-Many** with `ratings`: A restaurant can have many ratings.
- **One-to-Many** with `operatinghours`: A restaurant can have multiple operating hours.

---

## 2. `categories` Table
This table stores information about food or restaurant categories, such as Food, Drinks, etc.

### Key Columns:
- **id**: Primary key of the table.
- **name**: Name of the category.

### Relationships:
- **One-to-Many** with `places`: A category can be used by many restaurants. This relationship is defined by the `category_id` in the `places` table.

---

## 3. `kecamatan` Table
This table stores data about districts (kecamatan).

### Key Columns:
- **id**: Primary key of the table.
- **name**: Name of the district.

### Relationships:
- **One-to-Many** with `places`: A district can have many restaurants. This relationship is defined by the `kecamatan_id` in the `places` table.

---

## 4. `ratings` Table
This table stores restaurant ratings and the number of reviews.

### Key Columns:
- **id**: Primary key of the table.
- **place_id**: Foreign key referencing the `places` table (indicating the restaurant being rated).
- **rating**: Rating value of the restaurant (decimal number).
- **reviews**: Number of reviews for the restaurant.

### Relationships:
- **Many-to-One** with `places`: Many ratings are associated with one restaurant.

---

## 5. `operatinghours` Table
This table stores the operating hours for each restaurant based on the day.

### Key Columns:
- **id**: Primary key of the table.
- **place_id**: Foreign key referencing the `places` table (indicating the restaurant).
- **day**: The operational day (Monday, Tuesday, etc.).
- **opening_time**: Opening time of the restaurant.
- **closing_time**: Closing time of the restaurant.

### Relationships:
- **Many-to-One** with `places`: Many operating hours are associated with one restaurant.

---

## Relationships Between Tables

- **`places`** is the central table:
  - It connects to the `categories` table through the `category_id`.
  - It connects to the `kecamatan` table through the `kecamatan_id`.
  - It connects to the `ratings` table through the `place_id`.
  - It connects to the `operatinghours` table through the `place_id`.

- **`categories`** serves as a reference for restaurant categories, used in the `places` table to categorize restaurants.
- **`kecamatan`** serves as a reference for the location of each restaurant, stored in the `places` table.
- **`ratings`** stores feedback on each restaurant and links to `places` via the `place_id`.
- **`operatinghours`** stores the operational hours of each restaurant and is connected to `places` via the `place_id`.

---

## Example Relational Diagram
places ↔ categories (1 category, many places) categories.id ↔ places.category_id

places ↔ kecamatan (1 kecamatan, many places) kecamatan.id ↔ places.kecamatan_id

places ↔ ratings (1 place, many ratings) places.id ↔ ratings.place_id

places ↔ operatinghours (1 place, many operating hours) places.id ↔ operatinghours.place_id

---

## **Deployment Steps**

### **1. Cloud SQL Database Setup**

1. Create a **Cloud SQL (MySQL)** instance in the GCP Console.
2. Create the database and tables based on the schema provided above.
3. Configure database access for the app deployed in App Engine or Cloud Functions.
   
### **2. API Deployment to Google App Engine**

1. Set up your application in Google App Engine, using an `app.yaml` file for configuration.
2. Deploy your application to **App Engine** using the GCP CLI:
   ```bash
   gcloud app deploy
   ```
   
### **3. Cloud Run Deployment for ML API**

1. Create a **Cloud Run** for the prediction API.
2. Deploy the function using the GCP CLI:
   ```bash
   gcloud run deploy predict --runtime python39 --trigger-http --allow-unauthenticated
   ```
---

## **How to Run Locally**

1. Clone this repository to your local machine.
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database connection to **Cloud SQL** (use the connection string provided by GCP).
4. Run the application locally:
   ```bash
   python app.py
   ```
5. Test the endpoints using Postman or any API testing tool.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Open a pull request describing your changes.

---

## **License**

This project is licensed under the [MIT License](LICENSE).

For further questions, please contact the Cloud Computing team at kulinerkitaofficial28@gmail.com.
