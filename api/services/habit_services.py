from api.models.habit_tracker import HabitTracker

def get_habits(
    db, 
    selected_date, 
    completed
):

    query = db.query(HabitTracker)

    if selected_date is not None:
        query = query.filter(HabitTracker.date == selected_date)

    if completed is not None:
        query = query.filter(HabitTracker.completed == completed)

    habits = query.all()

    return habits