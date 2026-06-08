from fastapi import APIRouter, HTTPException
from datetime import date
from typing import Optional
from api.database import SessionLocal
from api.models.habit_tracker import HabitTracker
from api.schemas.habit_tracker import PostHabit, PutHabit
from api.services.habit_services import get_habits

habit_router = APIRouter(prefix="/api", tags=["HabitTracker"])

@habit_router.get("/")
def all_habits(
    selected_date: Optional[date] = None, 
    completed: Optional[bool] = None
):
    
    db = SessionLocal()
    habits = get_habits(db, selected_date, completed)
    db.close()

    return habits


@habit_router.post("/")
def post_habit(habit: PostHabit):
    
    db = SessionLocal()

    new_habit = HabitTracker(
        habit=habit.habit,
        date=habit.date, 
        completed=habit.completed
    )

    db.add(new_habit)
    db.commit()
    db.refresh(new_habit)

    db.close()

    return new_habit

@habit_router.put("/{habit_id}")
def update_habit(habit_id: int, habit: PutHabit):
    
    db = SessionLocal()

    existing_habit = db.query(HabitTracker).filter(HabitTracker.id == habit_id).first()

    if existing_habit is None:
        db.close()
        raise HTTPException(status_code=404, detail="Habit not found")
    
    if habit.habit is not None:
        existing_habit.habit = habit.habit

    if habit.date is not None:
        existing_habit.date = habit.date

    if habit.completed is not None:
        existing_habit.completed = habit.completed

    db.commit()
    db.refresh(existing_habit)

    db.close()

    return existing_habit

@habit_router.delete("/{habit_id}")
def delete_habit(habit_id: int):
    
    db = SessionLocal()
    
    existing_habit = db.query(HabitTracker).filter(HabitTracker.id == habit_id).first()

    if existing_habit is None:
        db.close()
        raise HTTPException(status_code=404, detail="Habit not found")
    

    db.delete(existing_habit)
    db.commit()

    db.close()

    return {"message": "Habit deleted successfully"}
