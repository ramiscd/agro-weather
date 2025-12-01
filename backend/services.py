import httpx
from datetime import datetime
from typing import Optional

async def get_coordinates(city: str) -> Optional[dict]:
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "en", "format": "json"}

    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    results = data.get("results")
    if not results:
        return None

    first = results[0]
    return {
        "latitude": first.get("latitude"),
        "longitude": first.get("longitude"),
        "name": first.get("name")
    }


async def get_weather(lat: float, lon: float) -> Optional[dict]:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "relativehumidity_2m,precipitation"
    }

    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    current = data.get("current_weather")
    hourly = data.get("hourly")
    if not current or not hourly:
        return None

    current_time = current["time"]
    target = datetime.fromisoformat(current_time)

    times = hourly.get("time", [])
    hour_times = [datetime.fromisoformat(t) for t in times]

    closest_idx = min(
        range(len(hour_times)),
        key=lambda i: abs(hour_times[i] - target)
    )

    humidity = hourly["relativehumidity_2m"][closest_idx]
    precipitation = hourly["precipitation"][closest_idx]

    return {
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "winddirection": current["winddirection"],
        "time": current["time"],
        "humidity": humidity,
        "precipitation": precipitation
    }
