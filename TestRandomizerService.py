import requests

minimum = 5
maximum = 20
response = requests.get(f"http://127.0.0.1:8000/random?minimum={minimum}&maximum={maximum}")
response = response.json()
randomNumber = (response["randomNumber"])
print(randomNumber)