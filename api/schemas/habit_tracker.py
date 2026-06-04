from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class HabitTrackerResponse(BaseModel):
    id: int
    task: str
    date: date
    completed: bool

    class Config:
        from_attributes = True

class PostHabit(BaseModel):
    task: str = Field(..., max_length=100)
    date: date
    completed: bool = False

class PutHabit(BaseModel):
    task: Optional[str] = Field(None, max_length=100)
    date: Optional[date] = None
    completed: Optional[bool] = None

    