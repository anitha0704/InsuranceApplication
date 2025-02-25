# Insurance Policy Management Application #

## Overview ##

This project is a full-stack Insurance Policy Management application built using:

   > Backend: FastAPI with SQLite3

   > Frontend: React.js with basic CSS

   > Deployment: ?

### The application provides functionalities to: ###

  1. Fetch all insurance policies
  2. Search policies by name (partial matches included)
  3. Filter policies by premium range, policy type, and coverage amount
  4. Sort policies by premium (ascending)

## Setup Instructions ##

### Backend Setup (FastAPI + SQLite3): ###

#### Clone the repository:

```
git clone git@github.com:anitha0704/InsuranceApplication.git
```


##### Create and activate a virtual environment:

```python -m venv venv```

```source venv/bin/activate```

##### Install dependencies:

```pip install -r requirements.txt```

##### Run the FastAPI server in terminal:

```uvicorn main:app --reload```

##### The server will be available at http://127.0.0.1:8000.

### Test API Endpoints:

Open ```http://127.0.0.1:8000/docs``` for interactive Swagger UI.

Use tools like Postman or Curl to test API responses.

### Frontend Setup (React.js + npm):

Navigate to the frontend directory in your terminal:

```cd insurance_ui```

Install Node.js (if not installed):
download and install Node.js (LTS version) from https://nodejs.org/.


Install dependencies: ```npm install```

Run the React development server: ```npm start```

The application will be accessible at ```http://localhost:3000```

### Implementation Approach:

1. Backend (FastAPI & SQLite3)

    1. Uses FastAPI to create RESTful endpoints.
    2. SQLite3 is used as a lightweight database.
    3. Provides endpoints for retrieving policies, searching, and filtering.

2. Frontend (React.js)

    1. Built as a Single Page Application (SPA).
    2. It uses Axios to fetch data from the backend API.
    3. Provides a search bar and filters for policy selection.
    4. Displays policies in a responsive table with sorting capabilities.

### Testing:

Backend testing is done using pytest.

Please make sure the backend is running before testing frontend components.

Deployment:

Backend: Deployed using AWS Lambda (can also run locally with SQLite3).

Frontend: Hosted on Vercel or Render for easy access.
