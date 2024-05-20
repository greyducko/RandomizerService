# RandomizerService
Randomizer microservice that returns a random integer between the minimum and maximum parameters

# How to run the microservice
1. Clone and navigate to the directory in your terminal.
2. Use the following line to start the microservice using uvicorn:
```
py -m uvicorn RandomizerService:RandomizerService --reload
```
3. By default, it runs on localhost 127.0.0.1:8000. 

# To programmatically REQUEST data:
1. Make a request to the following URI with a minimum and maximum parameter: http://127.0.0.1:8000/random?minimum={minimum}&maximum={maximum}
Note: You may need to change the host/port if not running with default settings. 
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
dictionary with the key "randomNumber" to access the random number that was generated. The following example in Python also shows how you can print the output.

```
import requests

minimum = 5
maximum = 20
response = requests.get(f"http://127.0.0.1:8000/random?minimum={minimum}&maximum={maximum}")
output = response.json()
print(output)
```
