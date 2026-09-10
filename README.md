# MailBrain

**Think Less. Mail Smarter.**

MailBrain is a Python backend project for an email productivity assistant. It's built with FastAPI, SQLAlchemy, and JWT authentication, and implements user accounts, full email CRUD, and rule-based email intelligence (categorization, priority scoring, reply drafting, task extraction).

> 🚧 **Status: Active development, backend-only.** No frontend UI or real email provider integration (Gmail/Outlook) yet — see [Planned / In Progress](#planned--in-progress).

---

## Current Implementation

### Authentication
- **User registration** (`POST /register`) — with password length validation (min 8 chars)
- **User login** (`POST /login`) with JWT access token issuance
- Password hashing via `passlib` (bcrypt)
- JWT creation/verification via `python-jose`

### Email management (full CRUD, all scoped to the authenticated user)
- Add, list (with filters: read/important/requires-action/search/priority/category), get single, update, delete
- Mark as read / mark as important
- Aggregate statistics endpoint (`GET /emails/statistics`)

### Email intelligence
- `POST /emails/analyze` — categorizes an email (work / college / finance / promotions / personal / other), scores priority (high/medium/low), flags whether it requires action, and produces a summary
- `POST /emails/{id}/generate-reply` — drafts a reply
- `POST /emails/{id}/extract-tasks` — pulls action items and day-of-week deadlines out of the email body

**Honesty note:** these three endpoints are currently **rule-based** (keyword matching + regex), not calls to an LLM — there's no OpenAI/Anthropic dependency in `requirements.txt` yet. They work, and they're a reasonable v1, but if you're evaluating this as an "AI" project: the intelligence layer today is deterministic pattern matching, not machine learning. Swapping the rule engine in `services/ai_service.py` for a real LLM call is the top item in the roadmap below.

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Backend Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite by default; configurable via `DATABASE_URL` env var (Postgres-ready) |
| Authentication | JWT (python-jose), password hashing (passlib/bcrypt) |
| Testing | pytest (dependency installed; automated test suite not yet written) |

## Project Structure

```
backend/app/
├── api/          # FastAPI route definitions (auth_routes.py, routes.py)
├── core/         # Auth dependency, JWT handling, password hashing, env-based config
├── database/     # SQLAlchemy models, engine/session (connection.py)
├── schemas/      # Pydantic request/response schemas, with input validation
└── services/     # Business logic — user_service, email_service, ai_service (rule-based)
```

## Setup

```bash
# Clone the repository
git clone https://github.com/MukeshK25-dev/MailBrain.git
cd MailBrain

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# then edit .env: set SECRET_KEY (generate with: python -c "import secrets; print(secrets.token_hex(32))")

# Run the development server
uvicorn backend.app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs at `http://127.0.0.1:8000/docs`.

`DATABASE_URL` is optional — omit it and the app uses a local `mailbrain.db` SQLite file automatically.

## Planned / In Progress

- Replace the rule-based analysis engine with a real LLM call (OpenAI/Anthropic API)
- Automated tests with `pytest` (dependency is already installed, no tests written yet)
- Gmail OAuth integration and real inbox sync
- Frontend interface
- PostgreSQL in production, SQLite only for local dev
- Rate limiting and structured logging

See the full product plan in [`docs/`](./docs):
- [Project Vision](./docs/01_Project_vision.md)
- [Product Requirements](./docs/02_PRD.md)
- [Roadmap](./docs/03_Roadmap.md)
- [Architecture](./docs/04_Architecture.md)
- [Database Design](./docs/05_Database_Design.md)

## License

See [LICENSE](./LICENSE).
