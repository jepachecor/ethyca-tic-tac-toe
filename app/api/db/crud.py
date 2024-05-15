from sqlalchemy.orm import Session
from app.api.models import *
from app.api.schemas import *
from sqlalchemy import desc

def get_user_by_username(db: Session, username: str):
    return db.query(player_model.Player).filter(player_model.Player.username == username).first()

def get_user_by_id(db: Session, id: int):
    return db.query(player_model.Player).filter(player_model.Player.id == id).first()

def create_player(db: Session, player: player_schema.PlayerIn):
    db_user = player_model.Player(
        username = player.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_game(db: Session, game: game_schema.GameIn):
    db_game = game_model.Game(
        player_id = game.player_id
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def list_games_by_player(db: Session, player_id: int):
    player = get_user_by_id(db=db, id=player_id)
    if player:
        return db.query(game_model.Game).filter_by(player_id=player_id).order_by(desc(game_model.Game.timestamp)).all()
    return None