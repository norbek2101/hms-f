from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import DATABASE_URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


# Create a new database engine
# engine = create_engine(DATABASE_URL)


DATABASE_URL = "postgresql+asyncpg://norbek:Qwerty123!@localhost/hms_db"

engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


# Base model class
Base = declarative_base()

# Dependency function for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
