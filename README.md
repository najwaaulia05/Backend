# **KulinerKita - Cloud Computing Documentation**

## **Overview**

KulinerKita is a cloud-based platform that allows users to search for, rate, and get information about dining places around them. This project utilizes Google Cloud Platform (GCP) technologies, such as **Cloud SQL** for database management and **App Engine** for app deployment, to build a scalable and robust web application.

## **Table of Contents**

1. [Cloud Architecture](#cloud-architecture)
2. [Database Schema](#database-schema)
3. [API Documentation](#api-documentation)
4. [Deployment Steps](#deployment-steps)
5. [How to Run Locally](#how-to-run-locally)

---

## **Cloud Architecture**

The **KulinerKita** application uses several services from **Google Cloud Platform (GCP)** to support its functionalities and scalability. The services include:

- **Cloud SQL (MySQL)** for relational database management.
- **Google App Engine** for deploying the web application and APIs automatically.
- **Google Cloud Storage** for storing image and media data.
- **Cloud Functions** for event-driven backend functions.

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

## **API Documentation**

The KulinerKita application provides several APIs for accessing dining place data and submitting ratings. Below are the available endpoints:

---

### **Authentication and Data API**

| **Endpoint**           | **Method** | **Description**                                         |
|-------------------------|------------|---------------------------------------------------------|
| `/login`               | POST       | Logs in a user and returns an authentication token.     |
| `/banners`             | GET        | Retrieves a list of promotional banners.               |
| `/categories`          | GET        | Retrieves a list of dining categories.                 |
| `/restaurants/nearby`  | GET        | Retrieves nearby dining places based on latitude and longitude. |
| `/restaurants/search`  | GET        | Searches for dining places by name or category.        |
| `/restaurants/{id}`    | GET        | Retrieves detailed information for a specific restaurant by ID. |
| `/ratings/{place_id}`  | POST       | Submits ratings and reviews for a specific dining place.|

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

### **3. Cloud Function Deployment for ML API**

1. Create a **Cloud Function** for the image prediction API.
2. Deploy the function using the GCP CLI:
   ```bash
   gcloud functions deploy predictImage --runtime python39 --trigger-http --allow-unauthenticated
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

## **License**

This project is licensed under the [MIT License](LICENSE).

For further questions, please contact the Cloud Computing team at KulinerKita.
