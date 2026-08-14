import os
from dotenv import load_dotenv

load_dotenv()

# Secret key for JWT — loaded from environment, never hardcoded
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError(
        "SECRET_KEY is not set. Create a .env file with SECRET_KEY=<your-secret> "
        "(see .env.example)."
    )

# Algorithm
ALGORITHM = "HS256"

# Token expiry
ACCESS_TOKEN_EXPIRE_MINUTES = 60
