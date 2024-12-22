from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.models import User
from app.core.security import get_password_hash, verify_password
from app.db.database import get_db
from app.core.config import settings
import jwt
from datetime import datetime, timedelta

class AuthService:
    @staticmethod
    def register_user(email: str, password: str, db: Session):
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered.")

        hashed_password = get_password_hash(password)
        new_user = User(email=email, hashed_password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def authenticate_user(email: str, password: str, db: Session):
        user = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Invalid credentials.")
        return user

    @staticmethod
    def create_access_token(data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt