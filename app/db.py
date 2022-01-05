from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Raw SQL
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

SQLALCHEMY_DB_URL = f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"

engine = create_engine(SQLALCHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Raw SQL
# while True:
#     try:
#         conn = psycopg2.connect("host=localhost dbname=fastapi user=postgres")
#         cursor = conn.cursor(cursor_factory=RealDictCursor)
#         print("Database successfully connected!")
#         break
#     except Exception as error:
#         print("Connection to database failed.")
#         print("Error: ", error)
#         time.sleep(5)
