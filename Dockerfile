FROM python:slim

WORKDIR /named-entity-recognition

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /named-entity-recognition

# EXPOSE 9005:9005

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9005"]