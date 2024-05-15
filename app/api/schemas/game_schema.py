from pydantic import BaseModel
from typing import Optional

class GameIn(BaseModel):
    player_id : int

class Game(GameIn):
    id          : int

    class Config:
        orm_mode = True