from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.app.database.models import Email
from backend.app.schemas.email import EmailCreate, EmailUpdate
from backend.app.services.ai_service import analyze_email_content


def create_email(
    db: Session,
    email_data: EmailCreate,
    owner_id: int,
):
    analysis = analyze_email_content(
        sender=email_data.sender,
        subject=email_data.subject,
        body=email_data.body,
    )

    email = Email(
        sender=email_data.sender,
        recipient=email_data.recipient,
        subject=email_data.subject,
        body=email_data.body,
        is_read=email_data.is_read,
        is_important=analysis["is_important"],
        requires_action=analysis["requires_action"],
        priority=analysis["priority"],
        category=analysis["category"],
        owner_id=owner_id,
    )

    db.add(email)
    db.commit()
    db.refresh(email)

    return {
        "message": "Email added successfully",
        "email": {
            "id": email.id,
            "sender": email.sender,
            "recipient": email.recipient,
            "subject": email.subject,
            "body": email.body,
            "is_read": email.is_read,
            "is_important": email.is_important,
            "requires_action": email.requires_action,
            "priority": email.priority,
            "category": email.category,
            "owner_id": email.owner_id,
        },
    }


def get_emails(
    db: Session,
    owner_id: int,
    is_read: bool | None = None,
    is_important: bool | None = None,
    requires_action: bool | None = None,
    search: str | None = None,
    priority: str | None = None,
    category: str | None = None,
):
    query = db.query(Email).filter(
        Email.owner_id == owner_id
    )

    if is_read is not None:
        query = query.filter(
            Email.is_read == is_read
        )

    if is_important is not None:
        query = query.filter(
            Email.is_important == is_important
        )

    if requires_action is not None:
        query = query.filter(
            Email.requires_action == requires_action
        )

    if priority is not None:
        query = query.filter(
            Email.priority == priority
        )

    if category is not None:
        query = query.filter(
            Email.category == category
        )

    if search:
        search_text = f"%{search}%"

        query = query.filter(
            (Email.sender.ilike(search_text))
            | (Email.recipient.ilike(search_text))
            | (Email.subject.ilike(search_text))
            | (Email.body.ilike(search_text))
        )

    emails = query.order_by(
        Email.id.desc()
    ).all()

    return {
        "message": "Emails retrieved successfully",
        "emails": [
            {
                "id": email.id,
                "sender": email.sender,
                "recipient": email.recipient,
                "subject": email.subject,
                "body": email.body,
                "is_read": email.is_read,
                "is_important": email.is_important,
                "requires_action": email.requires_action,
                "priority": email.priority,
                "category": email.category,
                "owner_id": email.owner_id,
            }
            for email in emails
        ],
    }


def get_email(
    db: Session,
    email_id: int,
    owner_id: int,
):
    email = (
        db.query(Email)
        .filter(
            Email.id == email_id,
            Email.owner_id == owner_id,
        )
        .first()
    )

    if not email:
        raise HTTPException(
            status_code=404,
            detail="Email not found",
        )

    return {
        "message": "Email retrieved successfully",
        "email": {
            "id": email.id,
            "sender": email.sender,
            "recipient": email.recipient,
            "subject": email.subject,
            "body": email.body,
            "is_read": email.is_read,
            "is_important": email.is_important,
            "requires_action": email.requires_action,
            "priority": email.priority,
            "category": email.category,
            "owner_id": email.owner_id,
        },
    }


def update_email(
    db: Session,
    email_id: int,
    owner_id: int,
    email_data: EmailUpdate,
):
    email = (
        db.query(Email)
        .filter(
            Email.id == email_id,
            Email.owner_id == owner_id,
        )
        .first()
    )

    if not email:
        raise HTTPException(
            status_code=404,
            detail="Email not found",
        )

    update_data = email_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        if hasattr(email, field):
            setattr(email, field, value)

    db.commit()
    db.refresh(email)

    return {
        "message": "Email updated successfully",
        "email": {
            "id": email.id,
            "sender": email.sender,
            "recipient": email.recipient,
            "subject": email.subject,
            "body": email.body,
            "is_read": email.is_read,
            "is_important": email.is_important,
            "requires_action": email.requires_action,
            "priority": email.priority,
            "category": email.category,
            "owner_id": email.owner_id,
        },
    }


def delete_email(
    db: Session,
    email_id: int,
    owner_id: int,
):
    email = (
        db.query(Email)
        .filter(
            Email.id == email_id,
            Email.owner_id == owner_id,
        )
        .first()
    )

    if not email:
        raise HTTPException(
            status_code=404,
            detail="Email not found",
        )

    db.delete(email)
    db.commit()

    return {
        "message": "Email deleted successfully",
        "email_id": email_id,
    }


def mark_email_read(
    db: Session,
    email_id: int,
    owner_id: int,
    is_read: bool,
):
    email = (
        db.query(Email)
        .filter(
            Email.id == email_id,
            Email.owner_id == owner_id,
        )
        .first()
    )

    if not email:
        raise HTTPException(
            status_code=404,
            detail="Email not found",
        )

    email.is_read = is_read

    db.commit()
    db.refresh(email)

    return {
        "message": "Email read status updated successfully",
        "email": {
            "id": email.id,
            "subject": email.subject,
            "is_read": email.is_read,
            "owner_id": email.owner_id,
        },
    }


def mark_email_important(
    db: Session,
    email_id: int,
    owner_id: int,
    is_important: bool,
):
    email = (
        db.query(Email)
        .filter(
            Email.id == email_id,
            Email.owner_id == owner_id,
        )
        .first()
    )

    if not email:
        raise HTTPException(
            status_code=404,
            detail="Email not found",
        )

    email.is_important = is_important

    db.commit()
    db.refresh(email)

    return {
        "message": "Email importance status updated successfully",
        "email": {
            "id": email.id,
            "subject": email.subject,
            "is_important": email.is_important,
            "owner_id": email.owner_id,
        },
    }


def get_email_statistics(
    db: Session,
    owner_id: int,
):
    total_emails = (
        db.query(Email)
        .filter(Email.owner_id == owner_id)
        .count()
    )

    read_emails = (
        db.query(Email)
        .filter(
            Email.owner_id == owner_id,
            Email.is_read == True,
        )
        .count()
    )

    unread_emails = (
        db.query(Email)
        .filter(
            Email.owner_id == owner_id,
            Email.is_read == False,
        )
        .count()
    )

    important_emails = (
        db.query(Email)
        .filter(
            Email.owner_id == owner_id,
            Email.is_important == True,
        )
        .count()
    )

    action_required_emails = (
        db.query(Email)
        .filter(
            Email.owner_id == owner_id,
            Email.requires_action == True,
        )
        .count()
    )

    high_priority = (
        db.query(Email)
        .filter(
            Email.owner_id == owner_id,
            Email.priority == "high",
        )
        .count()
    )

    medium_priority = (
        db.query(Email)
        .filter(
            Email.owner_id == owner_id,
            Email.priority == "medium",
        )
        .count()
    )

    low_priority = (
        db.query(Email)
        .filter(
            Email.owner_id == owner_id,
            Email.priority == "low",
        )
        .count()
    )

    return {
        "message": "Email statistics retrieved successfully",
        "statistics": {
            "total_emails": total_emails,
            "read_emails": read_emails,
            "unread_emails": unread_emails,
            "important_emails": important_emails,
            "action_required_emails": action_required_emails,
            "high_priority": high_priority,
            "medium_priority": medium_priority,
            "low_priority": low_priority,
        }
    }
