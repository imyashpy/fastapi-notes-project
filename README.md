# fastapi-notes-project

A simple Notes API built using **FastAPI** and **MySQL**.  
This project was created to practice building APIs, working with routes, request models, and database CRUD operations.

---

## 🚀 Features Implemented

### ✔ Create a Note  
- Endpoint: `POST /notes`  
- Accepts `title` and `content`  
- Stores data in MySQL

### ✔ Get All Notes  
- Endpoint: `GET /notes`  
- Returns all notes from the database

### ✔ MySQL Connection  
- Using `mysql.connector`  
- Database: `notesdb`  
- Table: `notes`

### ✔ Pydantic Model  
- Used `BaseModel` to validate incoming data

---

## 📁 Project Structure

app/
├── database.py # MySQL connection
├── crud.py # Database operations
├── models.py # Pydantic Note model
└── main.py # FastAPI routes


---

## 🛠 Tech Stack

- **FastAPI**
- **MySQL**
- **Pydantic**
- **Uvicorn (for local server)**

---

## ▶ How to Run Locally

1. Install requirements:
pip install fastapi mysql-connector-python uvicorn


2. Run the server:
uvicorn app.main:app --reload


3. Open API Docs:
http://127.0.0.1:8000/docs


---

## 📝 Status
This project currently includes:
- API setup  
- Create & Get Note routes  
- MySQL CRUD functionality  

More features like update, delete, auth (JWT), etc. may be added later.

---



