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

@router.get('/game/{game_id}/moves')
async def list_moves(game_id: int, db: Session = Depends(get_db)):
    moves_by_game = crud.get_moves_by_game(db=db, game_id=game_id)
    if not moves_by_game:
        raise HTTPException(status_code=400, detail='No moves on this game')
    return moves_by_game