from fastapi import FastAPI
from services import get_coordinates

app = FastAPI()

@app.get("/")
def ping():
    return {"message": "pong"}

@app.get("/geo")
async def geo(city: str):
    coords = await get_coordinates(city)
    return {"coords": coords}