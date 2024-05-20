# RandomizerService
Randomizer microservice that returns a random integer between the minimum and maximum parameters (also integers).

# How to run the microservice
1. Clone and navigate to the directory in your terminal.
2. Use the following line to start the microservice using uvicorn:
```
py -m uvicorn RandomizerService:RandomizerService --reload
```
3. By default, it runs on the host and port 127.0.0.1:8000. 

# To programmatically REQUEST data:
1. Make a request to the following URI with a minimum and maximum parameter:
```
http://127.0.0.1:8000/random?minimum={minimum}&maximum={maximum}
```
Note: You may need to change the host/port if not running with default settings. Minimum and maximum must be integers.

2. The following is an example of how to make a request in Python:
```
import requests

minimum = 5
maximum = 20
response = requests.get(f"http://127.0.0.1:8000/random?minimum={minimum}&maximum={maximum}")
```

# To programmatically RECEIVE data:
1. Simply save the request call to a variable as shown above. 
2. Format the response as JSON, and then you can additionally index the 
dictionary with the key "randomNumber" to access only the random number that was generated. 
Similarly, you can access only the error message (which you would receive if minimum and/or maximum are not integers) by indexing
the dictionary with the key "Error".
Otherwise, the response will be in normal JSON format. 

```
import requests

minimum = 5
maximum = 20
response = requests.get(f"http://127.0.0.1:8000/random?minimum={minimum}&maximum={maximum}")

response = response.json()

if "randomNumber" in response.keys():
    randomNumber = (response["randomNumber"])
else:
    error = (response["Error"])
```

# Sample responses after formatted as JSON:
```
Sample response where there is no error: {'randomNumber': 8}
Sample response when minimum and/or maximum parameter was not an integer: {'Error': 'Please ensure the parameters minimum and maximum are both integers.'}
```
