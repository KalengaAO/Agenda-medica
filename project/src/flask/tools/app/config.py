import os


class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "dev-secret"
    )

    DATABASE_PATH = os.getenv(
        "DATABASE_PATH",
        "/data/agenda.db"
    )

    API_BASE_URL = (
        f"http://{os.getenv('API_HOST', 'localhost')}:"
        f"{os.getenv('API_PORT', '5001')}"
    )

    API_TIMEOUT = float(
        os.getenv(
            "API_TIMEOUT",
            "5"
        )
    )