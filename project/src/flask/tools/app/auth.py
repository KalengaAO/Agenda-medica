import logging
import sqlite3

from werkzeug.security import check_password_hash

from .database import get_connection

logger = logging.getLogger(__name__)


class AuthError(Exception):
    """Erro esperado: credenciais inválidas ou dados de login ausentes."""


class DatabaseUnavailableError(Exception):
    """Erro de conexão/consulta ao banco de dados durante o login."""


def validate_login(identifier, password):
    """Valida usuário/e-mail e senha contra o banco de dados.

    Levanta AuthError para credenciais inválidas/ausentes e
    DatabaseUnavailableError para falhas de acesso ao banco.
    """
    if not identifier or not password:
        raise AuthError("Informe usuário/e-mail e senha.")

    try:
        conn = get_connection()
    except sqlite3.Error as exc:
        logger.error("Falha ao conectar ao banco durante o login: %s", exc)
        raise DatabaseUnavailableError("Não foi possível acessar o banco de dados.") from exc

    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM usuarios WHERE username = ? OR email = ?",
            (identifier, identifier),
        )
        user = cur.fetchone()
    except sqlite3.Error as exc:
        logger.error("Erro ao consultar usuário: %s", exc)
        raise DatabaseUnavailableError("Erro ao consultar o banco de dados.") from exc
    finally:
        conn.close()

    if user is None or not check_password_hash(user["password_hash"], password):
        logger.info("Tentativa de login inválida para identificador: %s", identifier)
        raise AuthError("Usuário ou senha inválidos.")

    return {"id": user["id"], "username": user["username"], "email": user["email"]}