import logging
import os
import sqlite3
from contextlib import contextmanager

from .config import Config

logger = logging.getLogger(__name__)


def get_connection():
    """Abre uma conexão com o banco SQLite, tratando erros de conexão."""
    try:
        os.makedirs(os.path.dirname(Config.DATABASE_PATH) or ".", exist_ok=True)
        conn = sqlite3.connect(Config.DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except sqlite3.Error as exc:
        logger.error("Erro ao conectar ao banco de dados: %s", exc)
        raise


@contextmanager
def db_cursor():
    """Context manager que garante commit/rollback e fechamento da conexão."""
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        yield cur
        conn.commit()
    except sqlite3.Error as exc:
        logger.error("Erro de banco de dados: %s", exc)
        if conn is not None:
            conn.rollback()
        raise
    finally:
        if conn is not None:
            conn.close()


def init_db():
    """Cria as tabelas necessárias caso ainda não existam."""
    with db_cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                criado_em TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )