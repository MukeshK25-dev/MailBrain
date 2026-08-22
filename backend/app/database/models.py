from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    username = Column(
        String,
        unique=True,
        index=True,
        nullable=False,
    )

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False,
    )

    password_hash = Column(
        String,
        nullable=False,
    )

    emails = relationship(
        "Email",
        back_populates="owner",
    )


class Email(Base):
    __tablename__ = "emails"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    sender = Column(
        String,
        nullable=False,
    )

    recipient = Column(
        String,
        nullable=False,
    )

    subject = Column(
        String,
        nullable=False,
    )

    body = Column(
        String,
        nullable=False,
    )

    is_read = Column(
        Boolean,
        default=False,
    )

    is_important = Column(
        Boolean,
        default=False,
    )

    requires_action = Column(
        Boolean,
        default=False,
    )

    priority = Column(
        String,
        default="medium",
        nullable=False,
    )

    category = Column(
        String,
        default="other",
        nullable=False,
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    owner = relationship(
        "User",
        back_populates="emails",
    )