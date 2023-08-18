from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    Date,
)
from database.database import get_session, get_engine_from_settings
from datetime import date

engine = get_engine_from_settings()
meta = MetaData()

score = Table(
    "score",
    meta,
    Column("id", Integer, primary_key=True),
    Column("player_name", String),
    Column("score", Integer),
    Column("date", Date, default=date.today()),
)

difficulty = Table(
    "params",
    meta,
    Column("id", Integer, primary_key=True),
    Column("easy", Boolean, default=False),
    Column("medium", Boolean, default=False),
    Column("hard", Boolean, default=False),
)

meta.create_all(engine)

print("done")
# TODO: table params avec toutes les potions de difficultés
