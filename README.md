📚 Library Management System

A Django REST Framework (DRF) based Library Management System that allows admins to manage books and users to browse available books. This project follows RESTful API principles and includes authentication, role-based access, and CRUD operations.

🚀 Features

✅ Admin Dashboard – Secure access for admins to manage books

✅ User Authentication – JWT-based authentication for security

✅ Book Management – CRUD operations for books

✅ API-Driven – Built using Django REST Framework (DRF)

✅ CSRF Protection – Secure API requests

✅ Docker Support – Optional containerization for easy deployment

📌 Technologies Used

Django 🐍

Django REST Framework (DRF)

JWT Authentication

📜 API Endpoints

Method	Endpoint -	Description

GET	/api/books/ -	Get all books

POST	/api/books/ -	Add a new book

GET	/api/books/<id>/ -	Get details of a book

PUT	/api/books/<id>/ -	Update a book

DELETE	/api/books/<id>/ -	Delete a book

GET	/api/admin-dashboard/ -	Admin Dashboard (JWT Protected)
