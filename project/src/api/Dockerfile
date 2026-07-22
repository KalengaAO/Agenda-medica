FROM python:3.12-slim

WORKDIR /app

COPY conf/requirements.txt ./conf/requirements.txt
RUN pip install --no-cache-dir -r conf/requirements.txt

COPY tools/ ./tools/

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/tools

WORKDIR /app/tools

RUN chmod +x entrypoint.sh

EXPOSE 5001

ENTRYPOINT ["./entrypoint.sh"]