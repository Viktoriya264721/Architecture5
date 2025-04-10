from fastapi import FastAPI
from typing import List

app = FastAPI()
db: List[dict] = []

@app.get("/")
def root():
    return {"description": "Stores dog data."}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/write")
def write_data(item: dict):
    db.append(item)
    return {"message": "Data written successfully."}

@app.get("/read")
def read_data():
    return {"data": db}
