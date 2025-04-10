from fastapi import FastAPI, Header, HTTPException
import requests

app = FastAPI()
APP_TOKEN = "Yourdog"

DB_URL = "http://localhost:8001"
BUSINESS_URL = "http://localhost:8002"

@app.get("/")
def root():
    return {"description": "Handles user requests"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/dog-info")
def process_dog_info(dog_data: dict, authorization: str = Header(None)):
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    requests.post(f"{DB_URL}/write", json=dog_data)
    response = requests.post(f"{BUSINESS_URL}/process", json=dog_data)
    processed_data = response.json()
    requests.post(f"{DB_URL}/write", json=processed_data)
    return processed_data
