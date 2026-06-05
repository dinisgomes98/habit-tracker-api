from api.models.habit_tracker import HabitTracker

def get_completed_habits(db):

    habits = db.query(HabitTracker).filter(
        HabitTracker.completed == True
    ).all()

    return habits