FROM python:3.11-slim AS base

<<<<<<< HEAD
=======
# Set work directory
>>>>>>> refs/remotes/origin/main
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

<<<<<<< HEAD
# Defina a variável de ambiente FLASK_APP
ENV FLASK_APP=run.py
=======
# Use gunicorn as the entrypoint, adjust the number of workers and threads as needed
CMD ["python", "flask", "run", "-b :5000", "app:app"]
>>>>>>> refs/remotes/origin/main

# Comando para iniciar o Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]

LABEL org.opencontainers.image.source https://github.com/GuilhermeFiorot/boliviamoveisbackend