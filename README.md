# MailBrain

**Think Less. Mail Smarter.**

MailBrain is a Python backend project for an AI-powered email productivity assistant. This repository currently implements the **authentication foundation** of the project — user registration, login, and JWT-based session handling — built with FastAPI and SQLAlchemy.

> 🚧 **Status: Early development.** Email integration, AI features, and the frontend described in the project vision are planned but not yet implemented. See [Current Implementation](#current-implementation) below for what actually exists today.

---

## Current Implementation

What's built and working right now:

- **User registration** (`POST /register`)
- **User login** (`POST /login`) with JWT access token issuance
- **Authenticated user lookup** (`GET /me`)
- Password hashing via `passlib`
- JWT creation/verification via `python-jose`
- SQLAlchemy ORM models backed by a SQLite database (development)

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Backend Framework | FastAPI |
| ORM | SQLAlchemy |
| Database (development) | SQLite |
| Authentication | JWT (python-jose), password hashing (passlib) |
| Testing | pytest (dependency installed; tests not yet implemented) |

## Project Structure

```
backend/app/
├── api/          # FastAPI route definitions
├── core/         # Auth, JWT handling, security, config
├── database/     # SQLAlchemy models, connection, session dependency
├── schemas/      # Pydantic request/response schemas
└── services/     # Business logic (user creation, authentication)
```

## Setup

```bash
# Clone the repository
git clone https://github.com/MukeshK25-dev/MailBrain.git
cd MailBrain

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn backend.app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs at `http://127.0.0.1:8000/docs`.

> **Note:** Before running, a `SECRET_KEY` must be configured for JWT signing. Environment-based configuration is planned — see project docs for details.

## Planned / In Progress

The following are part of the long-term project vision but are **not yet implemented** in this repository:

- Gmail OAuth integration and inbox access
- AI-powered email summarization and prioritization
- Spam/phishing detection
- Frontend interface
- PostgreSQL production database

See the full plan in [`docs/`](./docs):
- [Project Vision](./docs/01_Project_vision.md)
- [Product Requirements](./docs/02_PRD.md)
- [Roadmap](./docs/03_Roadmap.md)
- [Architecture](./docs/04_Architecture.md)
- [Database Design](./docs/05_Database_Design.md)

## License

See [LICENSE](./LICENSE).
