from secrets import choice
from typing import Optional
from fastapi import FastAPI
import string

app = FastAPI()

CHARS: str = string.ascii_letters + string.digits


@app.get("/generate/{length}/")
def generate_password(length: int):
    password: str = "".join([choice(CHARS) for _ in range(length + 1)])
    return {"generated_password": password}
