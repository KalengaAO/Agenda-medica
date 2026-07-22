#!/bin/sh
set -e

echo "[api] Iniciando serviço de API simulada de agendamentos..."
echo "[api] Dados mockados disponibilizados no momento da inicialização:"
python -c "from app.data import AGENDAMENTOS; import json; print(json.dumps(AGENDAMENTOS, ensure_ascii=False, indent=2))"

echo "[api] Subindo servidor HTTP na porta ${API_PORT:-5001}..."
exec gunicorn -b 0.0.0.0:${API_PORT:-5001} run:app