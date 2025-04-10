import requests

headers = {
    "Authorization": "Bearer Yourdog",
    "Content-Type": "application/json"
}

data = {
    "breed": "Beagle"
}

response = requests.post("http://localhost:8000/dog-info", headers=headers, json=data)

print("Response from Client Service:")
print(response.json())
