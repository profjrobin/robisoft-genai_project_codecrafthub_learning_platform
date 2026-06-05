# CodeCraftHub

A simple REST API project built with Python and Flask that allows developers to track courses they want to learn.

This project is designed for beginners who are learning:

* Python
* Flask
* REST APIs
* JSON data storage
* CRUD operations (Create, Read, Update, Delete)

Instead of using a database, course data is stored in a simple JSON file so you can focus on understanding REST API fundamentals.

---

# Project Overview

CodeCraftHub is a lightweight learning platform where developers can keep track of courses they plan to complete.

Each course contains:

* ID
* Course Name
* Description
* Target Completion Date
* Status
* Created Timestamp

Example:

```json
{
  "id": 1,
  "name": "Flask REST API Basics",
  "description": "Learn how to build REST APIs with Flask",
  "target_date": "2026-08-01",
  "status": "Not Started",
  "created_at": "2026-06-05T15:30:12.123456"
}
```

---

# Features

* Create new courses
* View all courses
* View a single course
* Update existing courses
* Delete courses
* Automatic course ID generation
* Automatic timestamp creation
* JSON file storage (no database required)
* Input validation
* Error handling
* Beginner-friendly code comments

---

# Technologies Used

* Python 3
* Flask
* JSON

---

# Project Structure

```text
codecrafthub/
│
├── app.py
├── courses.json
├── requirements.txt
└── README.md
```

### File Descriptions

#### app.py

Main Flask application.

Contains:

* REST API endpoints
* Validation logic
* JSON file operations
* Error handling

#### courses.json

Stores all course information.

Example:

```json
[
  {
    "id": 1,
    "name": "Flask Basics",
    "description": "Introduction to Flask",
    "target_date": "2026-08-01",
    "status": "In Progress",
    "created_at": "2026-06-05T15:30:12.123456"
  }
]
```

#### requirements.txt

Python package dependencies.

```text
Flask
```

#### README.md

Project documentation.

---

# Installation Instructions

## Step 1: Install Python

Verify Python is installed:

```bash
python --version
```

Expected output:

```bash
Python 3.x.x
```

If Python is not installed, download it from:

https://www.python.org/downloads

---

## Step 2: Create Project Folder

```bash
mkdir codecrafthub
cd codecrafthub
```

---

## Step 3: Create Virtual Environment (Recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 4: Install Flask

```bash
pip install Flask
```

---

## Step 5: Create requirements.txt

```bash
pip freeze > requirements.txt
```

---

## Step 6: Create app.py

Copy the provided Flask code into:

```text
app.py
```

---

# Running the Application

Start the Flask application:

```bash
python app.py
```

Expected output:

```text
* Running on http://127.0.0.1:5000
```

Open a browser:

```text
http://127.0.0.1:5000/courses
```

---

# API Documentation

Base URL:

```text
http://127.0.0.1:5000
```

---

## Get All Courses

### Request

```http
GET /courses
```

### Example

```bash
curl -X GET http://127.0.0.1:5000/courses
```

### Response

```json
[
  {
    "id": 1,
    "name": "Flask Basics",
    "description": "Learn Flask",
    "target_date": "2026-08-01",
    "status": "Not Started",
    "created_at": "2026-06-05T15:30:12.123456"
  }
]
```

---

## Get One Course

### Request

```http
GET /courses/{id}
```

### Example

```bash
curl -X GET http://127.0.0.1:5000/courses/1
```

---

## Create Course

### Request

```http
POST /courses
```

### Example

```bash
curl -X POST http://127.0.0.1:5000/courses \
-H "Content-Type: application/json" \
-d '{
"name":"Flask REST API Basics",
"description":"Learn REST APIs",
"target_date":"2026-08-01",
"status":"Not Started"
}'
```

---

## Update Course

### Request

```http
PUT /courses/{id}
```

### Example

```bash
curl -X PUT http://127.0.0.1:5000/courses/1 \
-H "Content-Type: application/json" \
-d '{
"name":"Advanced Flask",
"description":"Learn advanced Flask topics",
"target_date":"2026-09-01",
"status":"In Progress"
}'
```

---

## Delete Course

### Request

```http
DELETE /courses/{id}
```

### Example

```bash
curl -X DELETE http://127.0.0.1:5000/courses/1
```

---

# Course Status Values

The API only accepts the following values:

```text
Not Started
In Progress
Completed
```

Invalid example:

```text
Almost Done
```

---

# Testing Instructions

Follow this order:

### 1. View all courses

```bash
curl -X GET http://127.0.0.1:5000/courses
```

### 2. Create a course

```bash
curl -X POST http://127.0.0.1:5000/courses \
-H "Content-Type: application/json" \
-d '{
"name":"Python Basics",
"description":"Learn Python",
"target_date":"2026-08-01",
"status":"Not Started"
}'
```

### 3. View course

```bash
curl -X GET http://127.0.0.1:5000/courses/1
```

### 4. Update course

```bash
curl -X PUT http://127.0.0.1:5000/courses/1 \
-H "Content-Type: application/json" \
-d '{
"name":"Python Basics",
"description":"Learn Python Programming",
"target_date":"2026-08-15",
"status":"In Progress"
}'
```

### 5. Delete course

```bash
curl -X DELETE http://127.0.0.1:5000/courses/1
```

---

# Common Error Responses

## Missing Field

Response:

```json
{
  "error": "Missing required field: name"
}
```

---

## Invalid Status

Response:

```json
{
  "error": "Invalid status. Must be: Not Started, In Progress, or Completed"
}
```

---

## Invalid Date

Response:

```json
{
  "error": "target_date must be in YYYY-MM-DD format"
}
```

---

## Course Not Found

Response:

```json
{
  "error": "Course not found"
}
```

---

# Troubleshooting

## Flask Not Installed

Error:

```text
ModuleNotFoundError: No module named 'flask'
```

Solution:

```bash
pip install Flask
```

---

## Port Already In Use

Error:

```text
Address already in use
```

Solution:

Stop the application currently using port 5000 or change the Flask port.

Example:

```python
app.run(port=5001)
```

---

## Invalid JSON

Error:

```json
{
  "error": "Request body must be valid JSON"
}
```

Solution:

Verify:

* Quotes are correct
* JSON syntax is valid
* Content-Type header is set

Example:

```bash
-H "Content-Type: application/json"
```

---

## courses.json Corrupted

Error:

```text
Unable to read course data file
```

Solution:

Delete the file and restart the application.

```bash
rm courses.json
```

or

```cmd
del courses.json
```

The application will automatically recreate it.

---

# REST API Concepts Learned

By building this project you will learn:

* Flask basics
* Routing
* HTTP methods
* GET requests
* POST requests
* PUT requests
* DELETE requests
* JSON processing
* CRUD operations
* Input validation
* Error handling
* File storage
* API testing with curl

---

# Future Enhancements

After mastering this beginner version, consider adding:

* Search courses
* Filter by status
* Pagination
* User accounts
* SQLite database
* SQLAlchemy ORM
* JWT authentication
* Swagger/OpenAPI documentation
* Front-end interface using React or Vue

---

# License

This project is intended for educational purposes and learning REST API fundamentals with Python and Flask.
