from fastapi import APIRouter, Depends
from app.api.schemas import *
from app.api.db.database import get_db
from sqlalchemy.orm import Session
from app.api.models import *
from app.api.db import *

router = APIRouter()

@router.post("/move")
async def create_move(move: move_schema.MoveIn, db: Session = Depends(get_db)):

    return crud.create_move(db=db, move=move)
