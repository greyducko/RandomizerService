from fastapi import FastAPI
import random
RandomizerService = FastAPI()


@RandomizerService.get("/random")
def get_random(minimum: int, maximum: int):
    print("Request received. Responding with random number...")
    return {"randomNumber": random.randint(minimum, maximum)}
