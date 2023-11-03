import requests

parametros = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(
    url="https://opentdb.com/api.php?amount=10&type=boolean", params=parametros)
response.raise_for_status()

data = response.json()
question_data = data.get("results")
