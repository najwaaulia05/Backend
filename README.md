# KulinerKita-CC (# Team C242-PS155)  
Members of Cloud Computing for Bangkit Academy Capstone Team C242-PS155  

| Member                  | Student ID   | University                  | Status   |  
|:-----------------------:|:------------:|:---------------------------:|:--------:|  
| Dzaki Akmal Rabbani Alqadrie | C312B4KY1214 | Universitas Sebelas Maret  | Active   |  
| Fanes Arasadina          | C421B4KX1388 | STMIK Widya Utama           | Active   |  

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

The application uses **Cloud SQL (MySQL)** for structured data storage. Below are the main tables used in the KulinerKita database:

### **1. Categories Table**

- Stores categories of dining places (e.g., restaurant, cafe, street food).

|   **Column**   |        **Type**        |             **Description**                           |
| :------------: | :--------------------: | :---------------------------------------------------: |
| `id`           | INT (11, AUTO_INCREMENT) | Unique ID for each category.                        |
| `name`         | VARCHAR(50)            | Name of the category (e.g., Restaurant).              |
| `type`         | VARCHAR(50)            | Type of the category (foods or drinks).               |

### **2. Places Table**

- Stores information about dining places (name, category, operating hours, location).
  
|   **Column**            |          **Type**         |                  **Description**                         |
| :---------------------: | :-----------------------: | :------------------------------------------------------: |
| `id`                    | INT (11, AUTO_INCREMENT)  | Unique ID for each place.                                 |
| `name`                  | VARCHAR(255)              | Name of the place (e.g., restaurant, park, etc.).         |
| `address`               | TEXT                      | Address of the place.                                    |
| `phone_number`          | VARCHAR(20)               | Phone number of the place (optional).                    |
| `latitude`              | DOUBLE                    | Latitude coordinate of the place (optional).             |
| `longitude`             | DOUBLE                    | Longitude coordinate of the place (optional).            |
| `category_id`           | INT (11)                  | Reference to the category ID associated with the place.  |
| `categorize_weather`    | VARCHAR(50)               | Weather category of the place (optional).                |
| `maps_url`              | TEXT                      | URL to the location on maps (optional).                  |
| `min_price`             | INT (11)                  | Minimum price at the place (optional).                   |
| `max_price`             | INT (11)                  | Maximum price at the place (optional).                   |
| `kecamatan_id`          | INT (11)                  | ID of the sub-district or neighborhood (optional).       |
| `eco_friendly`          | TINYINT(1)                | Indicates if the place is eco-friendly (0 for No, 1 for Yes). |

### **3. OperatingHours Table**

- Stores the operating hours for each dining place.

|   **Column**       |       **Type**        |                  **Description**                             |
| :----------------: | :-------------------: | :----------------------------------------------------------: |
| `id`               | INT (11, AUTO_INCREMENT) | Unique ID for each operating hour record.                     |
| `place_id`         | INT (11)              | Reference to the place ID associated with the operating hours. |
| `day`              | VARCHAR(50)           | Day of the week (e.g., Monday, Tuesday, etc.).                |
| `opening_time`     | TIME                  | The opening time for the place on that specific day.          |
| `closing_time`     | TIME                  | The closing time for the place on that specific day.          |

### **4. Ratings Table**

- Stores ratings and reviews provided by users for dining places.

| **Column**  |   **Type**   |        **Description**         |
| :---------: | :----------: | :----------------------------: |
| `rating_id` |   INT (PK)   |       Unique rating ID.        |
| `place_id`  |   INT (FK)   |        Dining place ID.        |
|  `rating`   | DECIMAL(2,1) |      Rating value (0-5).       |
|  `review`   |     TEXT     | Review text provided by users. |

### **5. Sub-districts**

- Stores information about sub-districts (`kecamatan`) and their associated city/regency (`kab_kota`).

|   **Column**   |       **Type**        |                  **Description**                             |
| :------------: | :-------------------: | :----------------------------------------------------------: |
| `id`           | INT (11, AUTO_INCREMENT) | Unique ID for each sub-district (kecamatan).                   |
| `name`         | VARCHAR(255)           | Name of the sub-district (e.g., Kecamatan A).                  |
| `kab_kota`     | VARCHAR(255)           | Name of the associated city or regency (kabupaten/kota).       |

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
