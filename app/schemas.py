from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    phone: str = Field(..., description="Phone number with country code (e.g., +1234567890)")
    timezone: str = Field(default="UTC", description="User timezone")
    preferred_time: str = Field(default="09:00", description="Preferred time for daily SMS (HH:MM format)")


class UserUpdate(BaseModel):
    timezone: Optional[str] = None
    preferred_time: Optional[str] = None
    is_active: Optional[bool] = None


class UserResponse(BaseModel):
    id: int
    phone: str
    timezone: str
    preferred_time: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class QuoteResponse(BaseModel):
    id: int
    text: str
    author: str
    category: str

    class Config:
        from_attributes = True


class MessageResponse(BaseModel):
    id: int
    user_id: int
    quote_id: int
    sent_at: datetime
    delivery_status: str

    class Config:
        from_attributes = True
