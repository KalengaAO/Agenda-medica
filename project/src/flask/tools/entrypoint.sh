#!/bin/sh
set -e

echo "[flask] Preparando banco de dados (migração/seed)..."
python -m app.seed

echo "[flask] Iniciando aplicação Agenda Médica..."
exec gunicorn -c /app/conf/gunicorn.conf.py run:app