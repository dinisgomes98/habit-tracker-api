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

def get_stats(db):

    total_habits = db.query(HabitTracker).count()
    completed_habits = db.query(HabitTracker).filter(HabitTracker.completed == True).count()

    if total_habits == 0:
        completition_rate = 0
    else:
        completition_rate = completed_habits / total_habits * 100

    return {
        "total habits": total_habits,
        "completed habits": completed_habits,
        "completion rate": round(completition_rate, 2)
    }