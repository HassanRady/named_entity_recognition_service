# Named Entity Recognition Service from Text 

## What is it?
A microservice for identifying entities from text by Spacy. Accessed via an API.

## Documentation
<img src="assets/api.png">

POST request to ner endpoint:
```json
{
    "text": ["This is a test text", "This is another test text"]
}

```
succuss output (200):
```json
{
    "entities": ["word", "word"]
}
```

## Run
Two ways to run the api:

bash run.sh:
```sh
    $ python -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    $ uvicorn app:app --host 127.0.0.1 --port 9005 --reload
```
Or

docker container:
```docker
    $ docker build . -t ner-service
    $ docker run -p 9005:9005 -d --name ner-service ner-service
``` 

