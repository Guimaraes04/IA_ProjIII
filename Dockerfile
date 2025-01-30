FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm

COPY . .

# Definir variáveis de ambiente para as respostas
ENV TRANSLATE_ENTITIES y
ENV LIST_FEATURES y
ENV TRANSLATE_FEATURES y

CMD ["python", "main.docker.py"]