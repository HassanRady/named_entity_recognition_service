FROM python:3.9-slim

WORKDIR /src

COPY config.py .
COPY logger.py .
COPY main.py .
COPY ner_extractor.py .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

CMD ["python", "main.py"]