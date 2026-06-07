from api.models.habit_tracker import HabitTracker

def get_completed_habits(db):

    habits = db.query(HabitTracker).filter(
        HabitTracker.completed == True
    ).all()

    return habits

def get_habits_by_date(db, selected_date):

    habits = db.query(HabitTracker).filter(
        HabitTracker.date == selected_date
    ).all()

    return habits