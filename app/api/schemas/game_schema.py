from pydantic import BaseModel

class GameIn(BaseModel):
    player_id : int

class Game(GameIn):
    id          : int
    timestamp   : str

    class Config:
        orm_mode = True