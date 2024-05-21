import requests
import time

minimum = 5.5
maximum = 20

print("Making request...\n")
response = requests.get(f"http://127.0.0.1:8000/random?minimum={minimum}&maximum={maximum}")


time.sleep(2)
response = response.json()

print("Received data.\n")
time.sleep(1)
print(response)

if "randomNumber" in response.keys():
    print(response["randomNumber"])
else:
    print(response["Error"])


