import re


def analyze_email_content(
    sender: str,
    subject: str,
    body: str,
):
    """
    Analyze an email and determine:
    - summary
    - whether action is required
    - category
    - priority
    - importance
    """

    text = f"{subject} {body}".lower()

    action_keywords = [
        "reply",
        "respond",
        "response required",
        "action required",
        "please confirm",
        "please submit",
        "submit",
        "deadline",
        "due",
        "complete",
        "verify",
        "confirm",
        "register",
        "apply",
        "attend",
        "review",
        "payment due",
    ]

    requires_action = any(
        keyword in text
        for keyword in action_keywords
    )

    promotion_keywords = [
        "offer",
        "discount",
        "sale",
        "coupon",
        "deal",
        "promotion",
        "promotional",
        "unsubscribe",
        "limited time",
        "shop now",
        "special offer",
    ]

    finance_keywords = [
        "payment",
        "bank",
        "account",
        "transaction",
        "invoice",
        "salary",
        "refund",
        "money",
        "loan",
        "credit",
        "debit",
        "finance",
        "financial",
        "statement",
        "account statement",
        "bank statement",
    ]

    work_keywords = [
        "internship",
        "placement",
        "job",
        "career",
        "interview",
        "recruitment",
        "company",
        "office",
        "work",
        "employee",
        "employer",
        "hiring",
        "employment",
    ]

    college_keywords = [
        "college",
        "university",
        "assignment",
        "exam",
        "semester",
        "faculty",
        "professor",
        "project",
        "submission",
        "class",
        "department",
        "student",
        "campus",
        "academic",
        "attendance",
        "marks",
        "result",
    ]

    personal_keywords = [
        "birthday",
        "family",
        "friend",
        "personal",
        "vacation",
        "trip",
        "wedding",
        "invitation",
        "celebration",
        "party",
    ]

    if any(
        keyword in text
        for keyword in promotion_keywords
    ):
        category = "promotions"

    elif any(
        keyword in text
        for keyword in finance_keywords
    ):
        category = "finance"

    elif any(
        keyword in text
        for keyword in work_keywords
    ):
        category = "work"

    elif any(
        keyword in text
        for keyword in college_keywords
    ):
        category = "college"

    elif any(
        keyword in text
        for keyword in personal_keywords
    ):
        category = "personal"

    else:
        category = "other"

    high_priority_keywords = [
        "urgent",
        "emergency",
        "immediately",
        "asap",
        "deadline",
        "due today",
        "due tomorrow",
        "final notice",
        "action required",
        "respond immediately",
        "account suspended",
        "payment due",
        "fraud alert",
        "security alert",
    ]

    medium_priority_keywords = [
        "important",
        "interview",
        "exam",
        "submission",
        "application",
        "payment",
        "meeting",
        "reply",
        "response required",
        "please respond",
        "statement",
        "account",
    ]

    if any(
        keyword in text
        for keyword in high_priority_keywords
    ):
        priority = "high"

    elif any(
        keyword in text
        for keyword in medium_priority_keywords
    ):
        priority = "medium"

    else:
        priority = "low"

    if category == "promotions":
        priority = "low"

    if category == "personal":
        priority = "low"

    important_keywords = [
        "urgent",
        "emergency",
        "fraud alert",
        "security alert",
        "account suspended",
        "payment due",
        "final notice",
        "action required",
        "respond immediately",
        "deadline",
        "due today",
        "due tomorrow",
        "interview",
        "job offer",
        "internship offer",
        "important",
    ]

    is_important = any(
        keyword in text
        for keyword in important_keywords
    )

    if subject.strip():
        summary = subject.strip()
    else:
        words = body.strip().split()

        if len(words) <= 20:
            summary = body.strip()
        else:
            summary = " ".join(words[:20]) + "..."

    return {
        "summary": summary,
        "requires_action": requires_action,
        "category": category,
        "priority": priority,
        "is_important": is_important,
    }


def generate_email_reply(
    sender: str,
    subject: str,
    body: str,
):
    """
    Generate a simple AI reply
    based on email content.
    """

    text = f"{subject} {body}".lower()

    if (
        "interview" in text
        or "internship" in text
        or "job" in text
    ):
        reply = f"""
Dear Sir/Madam,

Thank you for your email regarding {subject}.

I appreciate the opportunity and confirm my interest.

Please let me know if any further information is required.

Regards,
Mukesh
"""

    elif (
        "project" in text
        or "assignment" in text
        or "submission" in text
    ):
        reply = f"""
Dear Sir/Madam,

Thank you for the reminder.

I will make sure the required work is completed and submitted on time.

Regards,
Mukesh
"""

    elif (
        "payment" in text
        or "invoice" in text
        or "bank" in text
    ):
        reply = f"""
Dear Sir/Madam,

Thank you for the information.

I have noted the details and will review them accordingly.

Regards,
Mukesh
"""

    else:
        reply = f"""
Dear Sir/Madam,

Thank you for your email.

I have received your message and will get back to you shortly.

Regards,
Mukesh
"""

    return {
        "reply": reply.strip()
    }


def extract_email_tasks(
    subject: str,
    body: str,
):
    """
    Extract tasks and deadlines from email.
    """

    text = f"{subject}. {body}"

    task_keywords = [
        "submit",
        "complete",
        "attend",
        "review",
        "register",
        "apply",
        "confirm",
        "verify",
        "reply",
        "respond",
        "pay",
    ]

    deadline_words = [
        "today",
        "tomorrow",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    tasks = []
    deadlines = []

    sentences = re.split(
        r"[.!?\n]+",
        text,
    )

    for sentence in sentences:
        sentence = sentence.strip()

        if not sentence:
            continue

        lower_sentence = sentence.lower()

        for keyword in task_keywords:
            if keyword in lower_sentence:
                tasks.append(sentence)
                break

        for day in deadline_words:
            if day in lower_sentence:
                deadlines.append(day.title())

    return {
        "tasks": list(set(tasks)),
        "deadlines": list(set(deadlines)),
        "task_count": len(set(tasks)),
    }