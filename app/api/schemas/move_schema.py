from pydantic import BaseModel

class MoveIn(BaseModel):
    x           : int
    y           : int
    game_id     : int
    player_id   : int

class Move(MoveIn):
    id          : int
    timestamp   : str

    class Config:
        orm_mode = True