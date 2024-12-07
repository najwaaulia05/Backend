# KulinerKita-CC (# Team C242-PS155)  
Members of Cloud Computing for Bangkit Academy Capstone Team C242-PS155  

| Member                  | Student ID   | University                  | Status   |  
|:-----------------------:|:------------:|:---------------------------:|:--------:|  
| Dzaki Akmal Rabbani Alqadrie | C312B4KY1214 | Universitas Sebelas Maret  | Active   |  
| Fanes Arasadina          | C421B4KX1388 | STMIK Widya Utama           | Active   |  

**This is the Cloud Computing repository for the KulinerKita application.**  

---  

# Restaurant Search API

A dynamic restaurant search API built with Node.js and Express. This API supports a wide range of filters for querying restaurants based on location, eco-friendliness, weather preferences, operating hours, ratings, reviews, and price range.

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
   git clone https://github.com/kulinerkita/restaurant-search-api.git
   cd restaurant-search-api
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
restaurant-search-api/
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

The application uses **Cloud SQL (MySQL)** for structured data storage. Below are the main tables used in the KulinerKita database:

### **1. Categories Table**

- Stores categories of dining places (e.g., restaurant, cafe, street food).

|  **Column**   |  **Type**   |             **Description**              |
| :-----------: | :---------: | :--------------------------------------: |
| `category_id` |  INT (PK)   |           Unique category ID.            |
|    `name`     | VARCHAR(50) | Name of the category (e.g., Restaurant). |
| `description` |    TEXT     |       Description of the category.       |

### **2. Places Table**

- Stores information about dining places (name, category, operating hours, location).

|  **Column**   |   **Type**   |          **Description**           |
| :-----------: | :----------: | :--------------------------------: |
|  `place_id`   |   INT (PK)   |      Unique dining place ID.       |
|    `name`     | VARCHAR(100) |     Name of the dining place.      |
| `category_id` |   INT (FK)   |  Category ID of the dining place.  |
|  `latitude`   | DECIMAL(9,6) | Latitude coordinate of the place.  |
|  `longitude`  | DECIMAL(9,6) | Longitude coordinate of the place. |

### **3. OperatingHours Table**

- Stores the operating hours for each dining place.

|  **Column**  | **Type** |        **Description**         |
| :----------: | :------: | :----------------------------: |
|  `hours_id`  | INT (PK) | Unique ID for operating hours. |
|  `place_id`  | INT (FK) |        Dining place ID.        |
|    `day`     |   ENUM   |        Day of the week.        |
| `open_time`  |   TIME   |   Opening time of the place.   |
| `close_time` |   TIME   |   Closing time of the place.   |

### **4. Ratings Table**

- Stores ratings and reviews provided by users for dining places.

| **Column**  |   **Type**   |        **Description**         |
| :---------: | :----------: | :----------------------------: |
| `rating_id` |   INT (PK)   |       Unique rating ID.        |
| `place_id`  |   INT (FK)   |        Dining place ID.        |
|  `rating`   | DECIMAL(2,1) |      Rating value (0-5).       |
|  `review`   |     TEXT     | Review text provided by users. |

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
