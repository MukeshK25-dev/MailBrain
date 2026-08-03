from sqlalchemy.orm import Session

from backend.app.core.security import hash_password, verify_password
from backend.app.database.models import User
from backend.app.schemas.user import UserCreate
from backend.app.schemas.login import UserLogin


def create_user(db: Session, user: UserCreate):
    """
    Create a new user in the database.
    """

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(db: Session, login_data: UserLogin):
    """
    Authenticate a user using email and password.
    """

    user = db.query(User).filter(User.email == login_data.email).first()

    if not user:
        return None

    if not verify_password(login_data.password, user.password_hash):
        return None

    return user