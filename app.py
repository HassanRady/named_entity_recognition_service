import uvicorn
from fastapi import FastAPI, Request
from main import *


app = FastAPI()

@app.post("/ner")
async def get_ner(request: Request):
    data = await request.json()
    ents = pipeline(data)
    return {"entities": ents}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9005)