from sqlalchemy.orm import Session
from passlib.context import CryptContext
from src.auth.models import User
from src.auth.schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash the password
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Create a new user
def create_user(db: Session, user_data: UserCreate):
    hashed_password = get_password_hash(user_data.password)
    db_user = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
