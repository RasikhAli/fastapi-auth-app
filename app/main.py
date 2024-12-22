from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth.routes import auth_router
from app.core.config import settings
from app.db.models import User  # Explicitly import User model
from app.db.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)



app = FastAPI(title="User Authentication App")

# Create tables
# Base.metadata.create_all(bind=engine)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth_router, prefix="/auth")

@app.get("/")
def root():
    return {"message": "Welcome to the Authentication App!"}