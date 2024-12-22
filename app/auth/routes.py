from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth.schemas import UserCreate, UserResponse, LoginRequest, Token
from app.auth.services import AuthService
from app.db.database import get_db

auth_router = APIRouter()

@auth_router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return AuthService.register_user(email=user.email, password=user.password, db=db)

@auth_router.post("/login", response_model=Token)
def login_user(login: LoginRequest, db: Session = Depends(get_db)):
    user = AuthService.authenticate_user(email=login.email, password=login.password, db=db)
    access_token = AuthService.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}