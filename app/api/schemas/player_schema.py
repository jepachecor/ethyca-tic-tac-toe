from pydantic import BaseModel

class PlayerIn(BaseModel):
    username : str

class Player(PlayerIn):
    id      : int    
    wins    : int
    losses  : int
    draws   : int

    class Config:
        orm_mode = True