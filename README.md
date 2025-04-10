
# Dog activity

A microservice-based system built with FastAPI that recommends **daily physical activity for a dog** based on its breed. The system consists of three services: **Client Service**, **Business Logic Service**, and **Database Service**.

---

## How to run the services

### Required Libraries:
```bash
pip install fastapi uvicorn requests
```
---

### Start Each Service in a Separate Terminal:

#### 1. Database Service (port 8001):
```bash
uvicorn db_service:app --port 8001
```

#### 2. Business Logic Service (port 8002):
```bash
uvicorn business_service:app --port 8002
```

#### 3. Client Service (port 8000):
```bash
uvicorn client_service:app --port 8000
```
---

## Token-Based Authentication

The Client Service requires a **token** in the `Authorization` header to process requests.

### Current token:
```
Authorization: Bearer Yourdog
```

---

## Request Flow

Here’s how a request flows through the system:

1. The **User** sends a request to the **Client Service** (`/dog-info`).
2. Client Service stores the original data in the **Database Service** (`/write`).
3. Then it sends the same data to the **Business Logic Service** (`/process`).
4. Business Logic Service returns the activity recommendation (e.g., "1+ hour").
5. Client Service stores the result again in the **Database Service**.
6. Finally, the Client Service returns the recommendation to the user.

### Diagram:
```
Client → Client Service → Database Service
                         ↓
                   Business Logic Service
                         ↓
                   Database Service → Client
```

## Example Usage

- In the first terminal, run Database Service:
```bash
uvicorn db_service:app --port 8001
```

- In the second terminal, run Business Logic Service:
```bash
uvicorn business_service:app --port 8002
```

- In the third terminal, run Client Service:
```bash
uvicorn client_service:app --port 8000
```

## Checking that the services are ‘alive’
Enter in your browser:
```bash
http://localhost:8000/health
```

```bash
http://localhost:8001/health
```

```bash
http://localhost:8002/health
```

Each status has to be 'ok'.

Once all services are running in separate terminals, you can test the system using a Python script.

###Python Test Script

There is a file called `test.py`, so run the script in the terminal:
```bash
python test_request.py
```

---

### Expected Output

```json
{
  "original": {"breed": "Beagle"},
  "breed_group": "Scent Hounds",
  "walk_recommendation": "1+ hour"
}
```
---
