from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.connection import get_db
from backend.app.schemas.user import UserCreate
from backend.app.schemas.login import UserLogin
from backend.app.services.user_service import create_user, authenticate_user

router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user)

    return {
        "message": "User registered successfully",
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email
    }


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(db, user)

    if authenticated_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful",
        "id": authenticated_user.id,
        "username": authenticated_user.username,
        "email": authenticated_user.email
    }