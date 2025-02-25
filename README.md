Insurance Policy Management Application

Overview

This project is a full-stack Insurance Policy Management application built using:

Backend: FastAPI with SQLite3

Frontend: React.js with basic CSS

Deployment: AWS Lambda (backend), Vercel/Render (frontend)

The application provides functionalities to:

Fetch all insurance policies

Search policies by name (partial matches included)

Filter policies by premium range, policy type, and coverage amount

Sort policies by premium (ascending/descending)

Setup Instructions

Backend Setup (FastAPI + SQLite3)

Clone the repository:

git clone <repository-url>
cd backend

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Run the FastAPI server:

uvicorn main:app --reload

The server will be available at http://127.0.0.1:8000.

Test API Endpoints:

Open http://127.0.0.1:8000/docs for interactive Swagger UI.

Use tools like Postman or Curl to test API responses.

Frontend Setup (React.js + npm)

Navigate to the frontend directory:

cd frontend

Install dependencies:

npm install

Run the React development server:

npm start

The application will be accessible at http://localhost:3000.

Implementation Approach

Backend (FastAPI & SQLite3)

Uses FastAPI to create RESTful endpoints.

SQLite3 is used as a lightweight database.

Provides endpoints for retrieving policies, searching, filtering, and sorting.

Implements async database operations for efficiency.

Uses Pydantic for data validation and type safety.

Frontend (React.js)

Built as a Single Page Application (SPA).

Uses Axios to fetch data from the backend API.

Provides a search bar and filters for policy selection.

Displays policies in a responsive table with sorting capabilities.

Testing

Backend testing is done using pytest.

Frontend testing can be performed with React Testing Library (npm test).

Ensure the backend is running before testing frontend components.

Deployment

Backend: Deployed using AWS Lambda (can also run locally with SQLite3).

Frontend: Hosted on Vercel or Render for easy access.
