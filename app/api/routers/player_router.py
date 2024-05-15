from fastapi import APIRouter, Depends, HTTPException
from app.api.schemas import *
from app.api.db.database import get_db
from sqlalchemy.orm import Session
from app.api.models import *
from app.api.db import *

router = APIRouter()

@router.post('/player', response_model=player_schema.Player)
async def create_player(player: PlayerIn, db: Session = Depends(get_db)):
    db_player = crud.get_user_by_username(db, username=player.username)

    if db_player:
        raise HTTPException(status_code=400, detail='Username exists!')

    return crud.create_player(db=db, player=player)

@router.get('/player/{player_id}/games')
async def list_games(player_id: int, db: Session = Depends(get_db)):
    games_by_player = crud.list_games_by_player(db=db, player_id=player_id)
    if not games_by_player:
        raise HTTPException(status_code=400, detail='No games for this user')
    return games_by_player