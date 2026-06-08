# Habit Tracker API

A REST API built with FastAPI to track habits and practice backend development concepts.

## Features

- Full CRUD operations
- SQLite database integration
- Request validation with Pydantic
- Modular API architecture
- Habit filtering endpoints
- Service layer separation
- Daily habit tracking
- Habit statistics endpoint

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```text
api/
├── models/
├── routes/
├── schemas/
├── services/
└── database.py

src/ 
└── main.py
```

## Purpose

This project was built to practice:
- Backend development
- REST APIs
- CRUD operations
- SQLAlchemy ORM
- Database integration
- API architecture
- Service layer separation
- Query filtering
- Request validation
- Basic analytics and statistics

## How to Run

Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
python main.py
```

## Available Endpoints

- `GET /api/`
- `POST /api/`
- `PUT /api/{habit_id}`
- `DELETE /api/{habit_id}`

## Filters

- `GET /api/?selected_date=YYYY-MM-DD`
- `GET /api/?completed=true`
- `GET /api/?selected_date=YYYY-MM-DD&completed=true`

## Specialized Endpoints

- `GET /api/today`
- `GET /api/stats`

## Example Stats Response

{
  "total habits": 10,
  "completed habits": 7,
  "completion rate": 70.0
}