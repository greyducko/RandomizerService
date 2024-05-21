from fastapi import FastAPI
import random
import time

RandomizerService = FastAPI()


@RandomizerService.get("/random")
def get_random(minimum, maximum):
    print("Request received...")
    time.sleep(2)
    try:

        minimum = int(minimum)
        maximum = int(maximum)
        print("Sending data...")
        time.sleep(1)
        return {"randomNumber": return_random_number(minimum, maximum)}

    except ValueError:
        print("Sending data...")
        time.sleep(1)
        return {"Error": error()}


def return_random_number(minimum, maximum):
    return random.randint(minimum, maximum)


def error():
    return "Please ensure the parameters minimum and maximum are both integers."
