from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.api.db.database import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    draws = Column(Integer, default=0)

    games = relationship('Game', back_populates='player')
    move = relationship('Move', back_populates='players')