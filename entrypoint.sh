#!/bin/bash
export HOST_CONNECTION="sqlite:///./db.db"
alembic upgrade head
uvicorn app.api.main:app --host=0.0.0.0 --port=8000