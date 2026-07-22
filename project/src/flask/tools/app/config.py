import os


class Config:
    """Configurações da aplicação, lidas de variáveis de ambiente para
    manter credenciais e dados sensíveis fora do código-fonte."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    DATABASE_PATH = os.environ.get("DATABASE_PATH", "/data/agenda.db")
    API_BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:5001")
    API_TIMEOUT = float(os.environ.get("API_TIMEOUT", "5"))