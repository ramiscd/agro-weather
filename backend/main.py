from fastapi import FastAPI, Query
from services import get_coordinates, get_weather
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weather")
async def weather(city: str = Query(..., min_length=2, max_length=50)):
    coords = await get_coordinates(city)
    if not coords:
        return {
            "success": False,
            "error": "City not found",
            "data": None
        }

    weather = await get_weather(coords["latitude"], coords["longitude"])
    if not weather:
        return {
            "success": False,
            "error": "Weather data unavailable",
            "data": None
        }

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
