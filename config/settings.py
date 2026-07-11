import os
from dotenv import load_dotenv

load_dotenv()


GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

DEFAULT_MODEL = os.getenv(
    "DEFAULT_MODEL",
    "gemini-2.5-flash"
)


CONTENT_BASE_URL = os.getenv(
    "CONTENT_BASE_URL"
)
