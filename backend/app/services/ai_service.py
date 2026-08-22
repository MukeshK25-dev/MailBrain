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

    # Analyze subject and body only.
    # Sender email addresses can accidentally contain keywords
    # such as "exam" inside domains like example.com.
    text = f"{subject} {body}".lower()

    # -----------------------------
    # ACTION DETECTION
    # -----------------------------

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

    # -----------------------------
    # CATEGORY CLASSIFICATION
    # -----------------------------

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

    # Check categories in order of specificity.
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

    # -----------------------------
    # PRIORITY CLASSIFICATION
    # -----------------------------

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

    # Promotional emails should normally be low priority.
    if category == "promotions":
        if any(
            keyword in text
            for keyword in high_priority_keywords
        ):
            priority = "high"
        else:
            priority = "low"

    # Personal emails should normally be low priority
    # unless they contain an explicitly urgent situation.
    if category == "personal":
        if any(
            keyword in text
            for keyword in high_priority_keywords
        ):
            priority = "high"
        else:
            priority = "low"

    # -----------------------------
    # IMPORTANCE CLASSIFICATION
    # -----------------------------

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

    # -----------------------------
    # SUMMARY
    # -----------------------------

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