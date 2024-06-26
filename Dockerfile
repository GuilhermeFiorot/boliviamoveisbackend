FROM python:3.11-slim AS base

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# Defina a variável de ambiente FLASK_APP
ENV FLASK_APP=run.py

# Comando para iniciar o Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]

LABEL org.opencontainers.image.source https://github.com/GuilhermeFiorot/boliviamoveisbackend