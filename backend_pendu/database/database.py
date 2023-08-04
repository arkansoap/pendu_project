# python C:\Users\arkan\dev_projects\pendu_project\backend_pendu\database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from local_settings import postgre_settings as settings
from environs import Env

env = Env()


def get_engine(user, password, host, port, db):
    url = f"{env('DATABASE')}://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(url=url)
    return engine


def get_engine_from_settings():
    engine = get_engine(
        user=settings["pguser"],
        password=settings["pgpwd"],
        host=settings["pghost"],
        port=settings["pgport"],
        db=settings["pgdb"],
    )
    return engine


def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session


if __name__ == "__main__":
    session = get_session()
    print(session)
