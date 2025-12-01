export type WeatherResponse = {
    city: string
    coordinates: {
      lat: number
      lon: number
    }
    weather: {
      temperature: number
      wind_speed: number
      wind_direction: number
      humidity: number
      precipitation: number
      time: string
    }
  }
  
  export type WeatherApiResponse = {
    success: boolean
    error: string | null
    data: WeatherResponse
  }
  