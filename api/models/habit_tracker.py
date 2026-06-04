from sqlalchemy import Boolean, Column, Integer, String, Date
from api.database import Base

class HabitTracker(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    habit = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    completed = Column(Boolean, default=False)