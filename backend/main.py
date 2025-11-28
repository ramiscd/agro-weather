from fastapi import FastAPI, Query
from services import get_coordinates, get_weather

app = FastAPI()

@app.get("/")
def ping():
    return {"message": "pong"}


@app.get("/weather")
async def weather(city: str = Query(..., min_length=2, max_length=50)):
    # Buscar coordenadas
    coords = await get_coordinates(city)
    if not coords:
        return {
            "success": False,
            "error": "City not found",
            "data": None
        }

    # Buscar clima
    weather = await get_weather(coords["latitude"], coords["longitude"])
    if not weather:
        return {
            "success": False,
            "error": "Weather data unavailable",
            "data": None
        }

    # Montar resposta limpa e amigável ao frontend
    response = {
        "city": coords["name"],
        "coordinates": {
            "lat": coords["latitude"],
            "lon": coords["longitude"]
        },
        "weather": {
            "temperature": weather["temperature"],
            "wind_speed": weather["windspeed"],
            "wind_direction": weather["winddirection"],
            "humidity": weather["humidity"],
            "precipitation": weather["precipitation"],
            "time": weather["time"]
        }
    }

    return {
        "success": True,
        "error": None,
        "data": response
    }
