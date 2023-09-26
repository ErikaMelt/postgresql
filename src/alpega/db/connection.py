import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


def create_database_connection():

    conn_str = os.getenv("DATABASE_URL")

    engine = create_engine(conn_str)
    Session = sessionmaker(bind=engine)

    return Session()
