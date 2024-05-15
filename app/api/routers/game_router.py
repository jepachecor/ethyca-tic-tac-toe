from fastapi import APIRouter, Depends, HTTPException
from app.api.schemas import *
from app.api.db.database import get_db
from sqlalchemy.orm import Session
from app.api.models import *
from app.api.db import *

router = APIRouter()

@router.post('/game', response_model=game_schema.Game)
async def create_game(game: game_schema.GameIn, db: Session = Depends(get_db)):

    return crud.create_game(db=db, game=game)