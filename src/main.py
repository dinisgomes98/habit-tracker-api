from fastapi import FastAPI
from api.routes.habit_tracker import habit_router
from api.database import Base, engine
from api.models.habit_tracker import HabitTracker

app = FastAPI()

app.include_router(habit_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def index():
    return {"status": "habit tracker api is running"}