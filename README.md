# FastAPI Authentication App

This is a user authentication application built with **FastAPI**. It includes features like user registration, login, and JWT-based authentication.

## Features

- **User Registration**: Register users with email and password.
- **User Login**: Authenticate users and provide JWT tokens.
- **Password Hashing**: Securely store passwords using hashing.
- **JWT Authentication**: Use JSON Web Tokens (JWT) for secure user sessions.
- **SQLite Database**: Lightweight database for storage.

---

## Project Structure

```
fastapi_auth_app/
├── app/
│   ├── __init__.py
│   ├── main.py                # Application entry point
│   ├── auth/                  # Authentication module
│   │   ├── __init__.py
│   │   ├── routes.py          # API endpoints for authentication
│   │   ├── schemas.py         # Pydantic models for validation
│   │   ├── services.py        # Business logic for auth
│   │   └── oauth.py           # OAuth utilities (if needed)
│   ├── core/                  # Core application logic
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration settings
│   │   └── security.py        # Password hashing and security
│   ├── db/                    # Database setup
│   │   ├── __init__.py
│   │   ├── database.py        # Database connection and session
│   │   └── models.py          # SQLAlchemy models
│   ├── static/                # Static files (CSS, JS, etc.)
│   └── templates/             # HTML templates (for frontend)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore rules
```

---

## Installation

### Prerequisites
- Python 3.10 or higher
- SQLite (bundled with Python)
- Git

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/RasikhAli/fastapi-auth-app.git
   cd fastapi-auth-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv app/venv
   source app/venv/bin/activate   # On Windows: app\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access the application at: [http://127.0.0.1:8000](http://127.0.0.1:8000) or  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 

---

## API Endpoints

### User Registration
- **Endpoint**: `/auth/register`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```

### User Login
- **Endpoint**: `/auth/login`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```

### JWT Authentication
- Use the token returned by `/auth/login` for secure endpoints by including it in the `Authorization` header:
  ```
  Authorization: Bearer <token>
  ```

---

## Configuration

### Environment Variables
Set environment variables in `app/core/config.py`:
```python
DATABASE_URL: str = "sqlite:///./app/test.db"
SECRET_KEY: str = "your-secret-key"
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
```

---

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

