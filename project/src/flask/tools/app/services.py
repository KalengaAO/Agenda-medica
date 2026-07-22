import logging

import requests

from .config import Config

logger = logging.getLogger(__name__)

REQUIRED_FIELDS = [
    "paciente",
    "cpf",
    "medico",
    "especialidade",
    "data",
    "horario",
    "convenio",
    "status",
]


class ApiUnavailableError(Exception):
    """A API de agendamentos está temporariamente indisponível (timeout,
    erro de conexão ou erro 5xx)."""


class InvalidApiResponseError(Exception):
    """A resposta da API é inválida (não é JSON) ou tem formato inesperado."""


def fetch_agendamentos(simulate=None):
    """Busca os agendamentos na API externa via requisição HTTP.

    Trata separadamente:
    - indisponibilidade temporária da API (timeout, conexão recusada, erro 5xx)
    - resposta vazia ou inválida (corpo não é JSON, ou não é uma lista)
    - campos obrigatórios ausentes em itens específicos (item é descartado
      e um aviso é registrado em log, sem quebrar a requisição inteira)
    """
    params = {"simulate": simulate} if simulate else None

    try:
        response = requests.get(
            f"{Config.API_BASE_URL}/agendamentos",
            params=params,
            timeout=Config.API_TIMEOUT,
        )
    except requests.Timeout as exc:
        logger.error("Timeout ao consultar a API de agendamentos: %s", exc)
        raise ApiUnavailableError("A API de agendamentos demorou demais para responder.") from exc
    except requests.ConnectionError as exc:
        logger.error("Erro de conexão com a API de agendamentos: %s", exc)
        raise ApiUnavailableError("Não foi possível conectar à API de agendamentos.") from exc
    except requests.RequestException as exc:
        logger.error("Erro inesperado ao consultar a API de agendamentos: %s", exc)
        raise ApiUnavailableError("Erro inesperado ao consultar a API de agendamentos.") from exc

    if response.status_code >= 500:
        logger.error("API de agendamentos retornou status %s", response.status_code)
        raise ApiUnavailableError("A API de agendamentos está indisponível no momento.")

    if response.status_code != 200:
        logger.error("API de agendamentos retornou status inesperado: %s", response.status_code)
        raise InvalidApiResponseError("A API retornou uma resposta inesperada.")

    try:
        data = response.json()
    except ValueError as exc:
        logger.error("Resposta da API não é um JSON válido: %s", exc)
        raise InvalidApiResponseError("A resposta da API não pôde ser interpretada.") from exc

    if data is None:
        logger.error("API de agendamentos retornou corpo vazio/nulo.")
        raise InvalidApiResponseError("A API retornou uma resposta vazia.")

    if not isinstance(data, list):
        logger.error("API de agendamentos retornou formato inesperado: %s", type(data))
        raise InvalidApiResponseError("Formato de resposta inesperado da API.")

    validados = []
    for item in data:
        if not isinstance(item, dict):
            logger.warning("Item de agendamento ignorado por não ser um objeto válido.")
            continue

        campos_ausentes = [
            campo for campo in REQUIRED_FIELDS if not item.get(campo)
        ]
        if campos_ausentes:
            logger.warning(
                "Agendamento descartado por campos obrigatórios ausentes: %s",
                campos_ausentes,
            )
            continue

        validados.append(item)

    return validados