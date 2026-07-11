import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

SECRET_KEY = os.getenv("SECRET_KEY")

DEFAULT_MODEL = os.getenv(
    "DEFAULT_MODEL",
    "gemini-2.5-flash"
)

GITHUB_OWNER = os.getenv(
    "GITHUB_OWNER"
)

GITHUB_REPOSITORY = os.getenv(
    "GITHUB_REPOSITORY"
)

CONTENT_BRANCH = os.getenv(
    "CONTENT_BRANCH",
    "content"
)
