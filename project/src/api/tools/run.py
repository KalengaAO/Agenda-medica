import json

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Ao ser iniciada diretamente pelo terminal, a aplicação também
    # entrega os dados mockados no console antes de subir o servidor.
    from app.data import AGENDAMENTOS

    print(json.dumps(AGENDAMENTOS, ensure_ascii=False, indent=2))
    app.run(host="0.0.0.0", port=5001)