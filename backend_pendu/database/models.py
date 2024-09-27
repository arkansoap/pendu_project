from sqlalchemy import Boolean, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()


class Difficulty(Base):
    __tablename__ = "params"

    id = Column(Integer, primary_key=True)
    easy = Column(Boolean, default=False)
    medium = Column(Boolean, default=False)
    hard = Column(Boolean, default=False)


class High_score(Base):
    __tablename__ = "score"

    id = Column(Integer, primary_key=True)
    player_name = Column(String, default="player")
    score = Column(Float, default=0)
    date = Column(Date, default=date.today())
