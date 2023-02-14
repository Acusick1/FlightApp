FROM python:3.10-slim

WORKDIR /usr

RUN apt-get update

COPY requirements ./requirements

RUN pip install --no-cache-dir -r requirements/prod.txt

ENV PYTHONPATH .

COPY config.py ./
COPY Procfile ./

COPY src ./src

CMD ["honcho", "start", "-f", "Procfile", "--port", "8000"]