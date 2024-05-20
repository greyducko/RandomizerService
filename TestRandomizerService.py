import requests

minimum = 5.5
maximum = 20

response = requests.get(f"http://127.0.0.1:8000/random?minimum={minimum}&maximum={maximum}")

print("Making request...\n")

response = response.json()

print("Received data.\n")

print(response)

# if "randomNumber" in response.keys():
#     print(response["randomNumber"])
# else:
#     print(response["Error"])


