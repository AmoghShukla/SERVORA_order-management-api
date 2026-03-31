from sqlalchemy import create_engine, sessionmaker
from sqlalchemy.orm import Session
import os
from src.config.config import Settings

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()