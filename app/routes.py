from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import User, Quote, Message
from app.schemas import UserCreate, UserUpdate, UserResponse, QuoteResponse, MessageResponse

router = APIRouter()


@router.post("/users", response_model=UserResponse, status_code=201)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """Register a new user with phone number and preferences"""
    existing_user = db.query(User).filter(User.phone == user_data.phone).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    user = User(
        phone=user_data.phone,
        timezone=user_data.timezone,
        preferred_time=user_data.preferred_time
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user details by ID"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users", response_model=List[UserResponse])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all users"""
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    """Update user preferences"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user_data.timezone is not None:
        user.timezone = user_data.timezone
    if user_data.preferred_time is not None:
        user.preferred_time = user_data.preferred_time
    if user_data.is_active is not None:
        user.is_active = user_data.is_active

    db.commit()
    db.refresh(user)
    return user


@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a user"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return None


@router.get("/quotes", response_model=List[QuoteResponse])
def list_quotes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all quotes"""
    quotes = db.query(Quote).offset(skip).limit(limit).all()
    return quotes


@router.get("/quotes/{quote_id}", response_model=QuoteResponse)
def get_quote(quote_id: int, db: Session = Depends(get_db)):
    """Get a specific quote"""
    quote = db.query(Quote).filter(Quote.id == quote_id).first()
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote


@router.get("/messages", response_model=List[MessageResponse])
def list_messages(user_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List message history, optionally filtered by user"""
    query = db.query(Message)
    if user_id:
        query = query.filter(Message.user_id == user_id)
    messages = query.offset(skip).limit(limit).all()
    return messages
