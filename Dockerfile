FROM python:3.9-slim

WORKDIR /src

COPY config.py .
COPY main.py .
COPY ner_extractor.py .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm


# EXPOSE 9005:9005

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9005"]