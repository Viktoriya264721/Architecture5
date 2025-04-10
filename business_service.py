from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"description": "Recommends dog walk time based on breed."}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process")
def process_data(payload: dict):
    breed = payload.get("breed", "").lower()

    breed_to_group = {
        "bernese mountain dog": "Working Dogs",
        "husky": "Working Dogs",
        "rottweiler": "Working Dogs",

        "greyhound": "Sight Hounds",
        "whippet": "Sight Hounds",
        "saluki": "Sight Hounds",

        "beagle": "Scent Hounds",
        "basset hound": "Scent Hounds",
        "bloodhound": "Scent Hounds",

        "jack russell": "Terriers",
        "border terrier": "Terriers",
        "fox terrier": "Terriers",

        "labrador": "Gundogs",
        "golden retriever": "Gundogs",
        "spaniel": "Gundogs",

        "pug": "Companion Dogs",
        "chihuahua": "Companion Dogs",
        "shih tzu": "Companion Dogs"
    }

    group_to_activity = {
        "Working Dogs": "1+ hour plus sport activity",
        "Sight Hounds": "2+ hours",
        "Scent Hounds": "1+ hour",
        "Terriers": "2 walks daily",
        "Gundogs": "2 walks daily",
        "Companion Dogs": "short daily walks"
    }

    group = breed_to_group.get(breed, "Unknown")
    recommendation = group_to_activity.get(group, "Consult a vet")

    result = {
        "original": payload,
        "breed_group": group,
        "walk_recommendation": recommendation
    }

    return result
