from sqlalchemy import DateTime, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.api.db.database import Base
from datetime import datetime

class Move(Base):
    __tablenema__ = 'move'

    id = Column(Integer, primary_key=True, index=True)
    x = Column(Integer)
    y = Column(Integer)
    timestamp = Column(DateTime, default=datetime.now)
    player_id = Column(Integer, ForeignKey('players.id'))
    game_id = Column(Integer, ForeignKey('games.id'))

    players = relationship('Player', back_populates='move')
    game = relationship('Game', back_populates='moves')