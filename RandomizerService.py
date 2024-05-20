from fastapi import FastAPI
import random
RandomizerService = FastAPI()


@RandomizerService.get("/random")
def get_random(minimum, maximum):
    print("Request received...")
    try:

        minimum = int(minimum)
        maximum = int(maximum)
        print("Sending data...")
        return {"randomNumber": return_random_number(minimum, maximum)}

    except ValueError:
        print("Sending data...")
        return {"Error": error()}


def return_random_number(minimum, maximum):
    return random.randint(minimum, maximum)


def error():
    return "Please ensure the parameters minimum and maximum are both integers."
