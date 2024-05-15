from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.api.db.database import Base
from datetime import datetime

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.now)
    player_id = Column(Integer, ForeignKey('players.id'))

    player = relationship('Player', back_populates='games')
    moves = relationship('Move', back_populates='game')