from sqlalchemy import Boolean, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Difficulty(Base):
    __tablename__ = "params"

    id = Column(Integer, primary_key=True)
    easy = Column(Boolean, default=False)
    medium = Column(Boolean, default=False)
    hard = Column(Boolean, default=False)
