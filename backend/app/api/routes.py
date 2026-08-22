from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.app.database.dependencies import get_db
from backend.app.database.models import User
from backend.app.schemas.email import EmailCreate, EmailUpdate
from backend.app.services.email_service import (
    create_email,
    get_emails,
    get_email,
    update_email,
    delete_email,
    mark_email_read,
    mark_email_important,
    get_email_statistics,
)
from backend.app.services.ai_service import analyze_email_content
from backend.app.core.auth import get_current_user

router = APIRouter()


@router.post("/emails")
def add_email(
    email_data: EmailCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_email(
        db=db,
        email_data=email_data,
        owner_id=current_user.id,
    )


@router.get("/emails")
def get_all_emails(
    is_read: bool | None = Query(default=None),
    is_important: bool | None = Query(default=None),
    requires_action: bool | None = Query(default=None),
    search: str | None = Query(default=None),
    priority: str | None = Query(default=None),
    category: str | None = Query(default=None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_emails(
        db=db,
        owner_id=current_user.id,
        is_read=is_read,
        is_important=is_important,
        requires_action=requires_action,
        search=search,
        priority=priority,
        category=category,
    )


@router.get("/emails/statistics")
def get_statistics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_email_statistics(
        db=db,
        owner_id=current_user.id,
    )


@router.get("/emails/{email_id}")
def get_single_email(
    email_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_email(
        db=db,
        email_id=email_id,
        owner_id=current_user.id,
    )


@router.put("/emails/{email_id}")
def update_email_route(
    email_id: int,
    email_data: EmailUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_email(
        db=db,
        email_id=email_id,
        owner_id=current_user.id,
        email_data=email_data,
    )


@router.delete("/emails/{email_id}")
def remove_email(
    email_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_email(
        db=db,
        email_id=email_id,
        owner_id=current_user.id,
    )


@router.patch("/emails/{email_id}/read")
def mark_email_read_route(
    email_id: int,
    is_read: bool,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return mark_email_read(
        db=db,
        email_id=email_id,
        owner_id=current_user.id,
        is_read=is_read,
    )


@router.patch("/emails/{email_id}/important")
def mark_email_important_route(
    email_id: int,
    is_important: bool,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return mark_email_important(
        db=db,
        email_id=email_id,
        owner_id=current_user.id,
        is_important=is_important,
    )


@router.post("/emails/analyze")
def analyze_email(
    email_data: EmailCreate,
    current_user: User = Depends(get_current_user),
):
    analysis = analyze_email_content(
        sender=email_data.sender,
        subject=email_data.subject,
        body=email_data.body,
    )

    return {
        "message": "Email analyzed successfully",
        "analysis": analysis,
    }