from flask import Blueprint, jsonify, request

from .data import AGENDAMENTOS

bp = Blueprint("api", __name__)


@bp.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@bp.get("/agendamentos")
def get_agendamentos():
    """
    Endpoint que entrega os dados mockados de agendamentos.

    Aceita um parâmetro opcional `simulate` para facilitar a reprodução
    de cenários de falha durante o desenvolvimento e os testes do
    consumidor (aplicação Flask principal):

    - simulate=error   -> responde 503 (indisponibilidade temporária)
    - simulate=empty   -> responde 200 com lista vazia
    - simulate=invalid -> responde 200 com corpo que não é um JSON válido
    - simulate=partial -> responde 200 com um item faltando campos obrigatórios
    """
    simulate = request.args.get("simulate")

    if simulate == "error":
        return jsonify({"erro": "Serviço de agendamentos indisponível"}), 503

    if simulate == "empty":
        return jsonify([]), 200

    if simulate == "invalid":
        return "isto-nao-e-um-json-valido", 200, {"Content-Type": "application/json"}

    if simulate == "partial":
        incompleto = dict(AGENDAMENTOS[0])
        incompleto.pop("cpf", None)
        return jsonify([incompleto]), 200

    return jsonify(AGENDAMENTOS), 200