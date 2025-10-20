# Library Management System API

This is the capstone project for the ALX Software Engineering program. It is a comprehensive REST API built with Django and Django REST Framework that provides backend services for a library management application.

## Project Overview

The API allows for managing books and users, and handles the core logic of checking out and returning books. It is designed following RESTful principles and includes features like user authentication, filtering, and automated API documentation.

---

## Features Implemented

* **Book Management:** Full CRUD (Create, Read, Update, Delete) functionality for library books.
* **User Management:** Full CRUD for library members, including secure registration with hashed passwords.
* **Loan Management:** Endpoints to handle book checkouts and returns, which automatically update a book's availability status.
* **API Filtering & Search:** The book list can be filtered by ISBN and searched by title or author.
* **Token Authentication:** Secure user authentication using DRF's built-in token system.
* **Automated Documentation:** Interactive API documentation is available via Swagger UI and ReDoc.

---

## API Endpoints

Here is a summary of the available endpoints.

### Authentication
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/accounts/register/` | Register a new user. |
| `POST` | `/api/accounts/login/` | Log in to get an auth token. |

### Books
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET`, `POST` | `/api/books/` | List all books or create a new book. |
| `GET`, `PUT`, `DELETE` | `/api/books/<id>/` | Retrieve, update, or delete a specific book. |
| `POST` | `/api/books/<id>/checkout/` | Check out a book (requires authentication). |
| `POST` | `/api/books/<id>/return/` | Return a book (requires authentication). |

---

## Technology Stack

* **Backend:** Python, Django, Django REST Framework
* **Database:** SQLite3 (for development)
* **Deployment:** Gunicorn, Heroku
* **API Documentation:** drf-yasg (Swagger UI)

---

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
    cd Library_Management_System
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
The API will be available at `http://127.0.0.1:8000/`.