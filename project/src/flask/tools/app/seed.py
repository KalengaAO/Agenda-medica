"""
Script de migração/seed do banco de dados.

Cria a tabela de usuários (caso não exista) e garante a existência de um
usuário de teste, usado para validar o fluxo de login da aplicação.

Uso:
    python -m app.seed
"""

import logging

from werkzeug.security import generate_password_hash

from .database import db_cursor, init_db

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

TEST_USER = {
    "username": "medico.teste",
    "email": "medico.teste@timesaver.com.br",
    "password": "Teste@123",
}


def seed():
    init_db()

    with db_cursor() as cur:
        cur.execute("SELECT id FROM usuarios WHERE username = ?", (TEST_USER["username"],))
        if cur.fetchone() is None:
            cur.execute(
                "INSERT INTO usuarios (username, email, password_hash) VALUES (?, ?, ?)",
                (
                    TEST_USER["username"],
                    TEST_USER["email"],
                    generate_password_hash(TEST_USER["password"]),
                ),
            )
            logger.info("Usuário de teste criado com sucesso: %s", TEST_USER["username"])
        else:
            logger.info("Usuário de teste já existia, nenhuma ação necessária.")


if __name__ == "__main__":
    seed()