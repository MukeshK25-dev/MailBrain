from pydantic import BaseModel
from typing import Literal


Priority = Literal["high", "medium", "low"]

Category = Literal[
    "work",
    "college",
    "personal",
    "finance",
    "promotions",
    "other",
]


class EmailCreate(BaseModel):
    sender: str
    recipient: str
    subject: str
    body: str
    is_read: bool = False
    is_important: bool = False


class EmailUpdate(BaseModel):
    sender: str | None = None
    recipient: str | None = None
    subject: str | None = None
    body: str | None = None
    is_read: bool | None = None
    is_important: bool | None = None
    priority: Priority | None = None
    category: Category | None = None