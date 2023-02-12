from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from local_settings import postgre_settings as settings


def get_engine(user, password, host, port, db):
    url = f"postgres+psycopg2://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(url=url)
    return engine
