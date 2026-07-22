import logging 
from functools import wraps

from flask import Blueprint, flash, jsonify, redirect, render_template, request, session, url_for

from .auth import AuthError, DatabaseUnavailableError, validate_login
from .services import ApiUnavailableError, InvalidApiResponseError, fetch_agendamentos

logger = logging.getLogger(__name__)
bp = Blueprint("main", __name__)


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("main.login"))
        return view(*args, **kwargs)

    return wrapped


@bp.route("/")
def index():
    if "user" in session:
        return redirect(url_for("main.agenda"))
    return redirect(url_for("main.login"))


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    identifier = request.form.get("identifier", "").strip()
    password = request.form.get("password", "")

    try:
        user = validate_login(identifier, password)
    except AuthError as exc:
        flash(str(exc), "error")
        return render_template("login.html"), 401
    except DatabaseUnavailableError as exc:
        logger.error("Banco de dados indisponível durante o login: %s", exc)
        flash("Serviço temporariamente indisponível. Tente novamente em instantes.", "error")
        return render_template("login.html"), 503

    session["user"] = user
    return redirect(url_for("main.agenda"))


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.login"))


@bp.route("/agenda")
@login_required
def agenda():
    return render_template("dashboard.html", user=session["user"])


@bp.route("/api/agendamentos")
@login_required
def api_agendamentos():
    simulate = request.args.get("simulate")
    try:
        agendamentos = fetch_agendamentos(simulate=simulate)
    except ApiUnavailableError as exc:
        return jsonify({"erro": str(exc)}), 503
    except InvalidApiResponseError as exc:
        return jsonify({"erro": str(exc)}), 502

    resposta = {"dados": agendamentos, "total": len(agendamentos)}
    if not agendamentos:
        resposta["mensagem"] = "Nenhum agendamento disponível no momento."

    return jsonify(resposta), 200


@bp.route("/api/agendamentos/busca")
@login_required
def buscar_agendamento():
    termo = request.args.get("q", "").strip()

    try:
        agendamentos = fetch_agendamentos()
    except ApiUnavailableError as exc:
        return jsonify({"erro": str(exc)}), 503
    except InvalidApiResponseError as exc:
        return jsonify({"erro": str(exc)}), 502

    if not termo:
        resposta = {"dados": agendamentos, "total": len(agendamentos)}
        if not agendamentos:
            resposta["mensagem"] = "Nenhum agendamento disponível no momento."
        return jsonify(resposta), 200

    termo_lower = termo.lower()
    resultados = [
        item
        for item in agendamentos
        if termo_lower in item["paciente"].lower()
        or termo_lower in item["cpf"].lower()
        or termo_lower in item["medico"].lower()
    ]

    if not resultados:
        return jsonify({"dados": [], "total": 0, "mensagem": "Nenhum registro encontrado."}), 200

    return jsonify({"dados": resultados, "total": len(resultados)}), 200