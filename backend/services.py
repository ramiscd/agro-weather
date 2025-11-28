import httpx

async def get_coordinates(city: str):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "en", "format": "json"}

    async with httpx.AsyncClient() as client:
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
