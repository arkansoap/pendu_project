# python C:\Users\arkan\dev_projects\pendu_project\backend_pendu\database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from local_settings import postgre_settings as settings


def get_engine(user, password, host, port, db):
    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
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
    engine = engine = get_engine(
        user=settings["pguser"],
        password=settings["pgpwd"],
        host=settings["pghost"],
        port=settings["pgport"],
        db=settings["pgdb"],
    )
    session = sessionmaker(bind=engine)()
    return session


if __name__ == "__main__":

    session = get_session()
    print(session)
