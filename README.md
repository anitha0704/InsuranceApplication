# Insurance Policy Management Application #

## Overview ##

A full-stack **Insurance Policy Management** application with a **FastAPI backend** and a **React.js frontend** deployed on **Railway**.

### The application provides functionalities to: ###

  1. Fetch all insurance policies
  2. Search policies by name (partial matches included)
  3. Filter policies by premium range, policy type, and coverage amount
  4. Sort policies by premium (ascending)

### Implementation Approach:

1. Backend (FastAPI & SQLite3)

   * Uses FastAPI to create REST endpoints.
   * SQLite3 is used as a lightweight database. 
   * Provides endpoints for retrieving policies, searching, and filtering.

2. Frontend (React.js)

   * Built as a Single Page Application (SPA). 
   * It uses Axios to fetch data from the backend API. 
   * Provides a search bar and filters for policy selection. 
   * Displays policies in a responsive table with sorting capabilities.

### Enhancements Implemented:
* **Error Handling**: Improved error handling in the backend to ensure stability
* **User Input Validation:**
  * When searching by name, only strings or alphanumeric values are accepted. 
  * If an integer is entered, the user is alerted.
* **Error Responses**:
  * Proper messages and status codes are returned to the UI for better debugging.
* **Flexible Filtering**: Filters are now optional, providing a smoother user experience.
* **Enhanced UI** - user-friendliness and accessibility.

## 🛠️ Setup & Deployment Guide

### 1️⃣ Prerequisites
* Before starting, ensure you have:
* Git installed (git --version)
* Python 3.8+ installed (python --version)
* Node.js 16+ installed (node -v)
* Install Node.js (if not installed): download and install Node.js (LTS version) from https://nodejs.org/.
* Railway CLI installed (npm install -g @railway/cli)
* A Railway account ([Sign up here](https://railway.app/))

### Backend (FastAPI) Setup

### 2️⃣ Clone the Repository

#### Clone the project
`git clone git@github.com:anitha0704/InsuranceApplication.git`

### 3️⃣ Set Up a Virtual Environment

`python -m venv venv`

`source venv/bin/activate`  # Mac/Linux

`venv\Scripts\activate`   # Windows

### 4️⃣ Install Dependencies

 `pip install -r requirements.txt`

### 5️⃣ Run the Backend Locally

*    `uvicorn application:app --reload`
*    The server will be available at http://127.0.0.1:8000.
*    📌 Access API Docs: Open http://127.0.0.1:8000/docs in your browser.

### 🚀 Deploy Backend to Railway

### 6️⃣ Create a Railway Project & Deploy

* `railway init` # Initialize Railway project (creates a new project)
* `railway link`  # Link to existing project (if applicable) 
* `railway up`  # Deploy backend

### 7️⃣ Set a Start Command in Railway Dashboard

   * Go to your Railway **Project → Settings**.

   * Find Start Command and set it to: 
 `uvicorn main:app --host 0.0.0.0 --port $PORT` - (replace main with your app name)

### 8️⃣ Get Deployed Backend URL

* After deployment, Railway will generate a public API URL or generate domain manually from settings
* Example: https://insurancepolicy-api.up.railway.app
* Replace this URL in the frontend API calls.

## 🔹 Frontend (React.js) Setup

### 9️⃣ Install Frontend Dependencies

*    `cd insurance-ui` - navigate to the frontend code folder
* `npm install`

### 🔟 Update API Base URL (in insurance-ui/src/components/InsuranceList.js)

* `const API_BASE_URL = "https://insurancepolicy-api.up.railway.app";` // Update with your backend URL

### 1️⃣1️⃣ Run Frontend Locally

   * `npm start`
   * 📌 **Access Frontend**: Open http://localhost:3000 in your browser.

## 🚀 Deploy Frontend to Railway

### 1️⃣2️⃣ Deploy Frontend to Railway

`railway init`  # Inside frontend folder

`railway up `   # Deploy frontend

### 1️⃣3️⃣ Get Deployed Frontend URL

After deployment, Railway will generate a public frontend URL.

**Example**: https://insuranceapplication-production.up.railway.app/

### ✅ Testing the Deployment

**Backend**: Visit https://insurancepolicy-api.up.railway.app/docs to test APIs.

**Frontend**: Visit https://insuranceapplication-production.up.railway.app/ to use the application.

### 📌 Troubleshooting:

Ensure **API URLs** in React match the deployed backend URL.

Enable **CORS** in FastAPI (application.py) to allow frontend requests.

If errors occur, check Railway logs: `railway logs`


