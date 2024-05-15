from sqlalchemy.orm import Session
from app.api.models import *
from app.api.schemas import *

def get_user_by_username(db: Session, username: str):
    return db.query(player_model.Player).filter(player_model.Player.username == username).first()

def create_player(db: Session, player: player_schema.PlayerIn):
    db_user = player_model.Player(
        username = player.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
