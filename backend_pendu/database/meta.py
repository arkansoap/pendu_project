from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

from database import get_session, get_engine_from_settings


engine = get_engine_from_settings()
meta = MetaData()

students = Table(
    "score",
    meta,
    Column("id", Integer, primary_key=True),
    Column("player_name", String),
    Column("score", Integer),
    Column("date", String),
)
meta.create_all(engine)

# TODO: table params
