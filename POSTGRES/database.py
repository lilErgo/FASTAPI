from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from POSTGRES.config import settings

# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-sqlalchemy-engine

engine = create_engine(
                            settings.DATABASE_URL_psycopg,
                            echo=True
                      )

session = sessionmaker(engine)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

def get_db_session() -> session:
    return session
