import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL — falls back to local SQLite file for development
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///mailbrain.db")

# SQLite requires this flag for use with multiple threads (FastAPI's default worker model)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Create the database engine
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
)

# Create database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
