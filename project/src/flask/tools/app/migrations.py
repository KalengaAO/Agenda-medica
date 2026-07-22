from .database import db_cursor



def init_db():

    with db_cursor() as cur:

        cur.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password_hash TEXT NOT NULL,

            criado_em TIMESTAMP
            DEFAULT CURRENT_TIMESTAMP
        )
        """
        )