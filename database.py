import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

load_dotenv()
DATABASE_URL =os.getenv("DATABASE_URL")
engine= create_engine(
    DATABASE_URL,

    pool_pre_ping=True
                      )
sessionlocal= sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()