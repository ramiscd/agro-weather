"use client";

import { useState } from "react";
import type { WeatherApiResponse, WeatherResponse } from "@/types/weather"

export default function Home() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState<WeatherResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSearch(e: React.FormEvent) {
    e.preventDefault();
    if (!city.trim()) return;

    setLoading(true);
    setError("");
    setWeather(null);

    try {
      const res = await fetch(`http://127.0.0.1:8000/weather?city=${encodeURIComponent(city)}`);
      const json = await res.json();

      if (!json.success) {
        setError("Erro ao buscar dados da cidade");
      } else {
        setWeather(json.data);
      }
    } catch (err) {
      setError("Falha ao conectar com o servidor");
    }

    setLoading(false);
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-300 to-blue-600 p-8 flex justify-center">
      <div className="w-full max-w-4xl">
        <h1 className="text-white text-center text-3xl font-bold mb-4">Buscador de clima</h1>
        <p className="text-white text-center text-lg mb-4">
          Busque o clima atual digitando o nome de uma cidade
        </p>
        <form onSubmit={handleSearch} className="flex gap-3 mb-8">
          <input
            type="text"
            placeholder="Digite uma cidade"
            className="flex-1 p-4 rounded-xl bg-white/70 backdrop-blur text-gray-800 outline-none"
            value={city}
            onChange={e => setCity(e.target.value)}
          />
          <button
            type="submit"
            className="px-6 py-3 rounded-xl bg-white/80 text-gray-900 hover:bg-white transition"
          >
            Buscar
          </button>
        </form>

        {loading && (
          <div className="flex justify-center items-center py-10">
            <div className="w-10 h-10 border-4 border-white/40 border-t-white rounded-full animate-spin"></div>
            <span className="ml-4 text-white text-lg">Carregando...</span>
          </div>
        )}


        {error && (
          <p className="text-red-200 text-lg">{error}</p>
        )}

        {weather && (
          <div className="relative p-10 rounded-3xl bg-white/20 backdrop-blur shadow-lg">
            <div
              className="absolute inset-0 bg-cover bg-center opacity-30 rounded-3xl"
              style={{
                backgroundImage: "url('/rain-texture.jpg')"
              }}
            />

            <div className="relative z-10 text-white">
              <h2 className="text-4xl mb-2">{weather.city}</h2>
              <p className="text-lg mb-8">{new Date(weather.weather.time).toLocaleString()}</p>

              <div className="flex items-center gap-12">
                <div>
                  <p className="text-7xl">{Math.round(weather.weather.temperature)}°</p>
                  <p className="text-xl mt-2">
                    Vento {weather.weather.wind_speed} km/h
                  </p>
                  <p className="text-xl">
                    Umidade {weather.weather.humidity} porcento
                  </p>
                  <p className="text-xl">
                    Precipitação {weather.weather.precipitation} mm
                  </p>
                </div>

                <div className="flex-1">
                  <div
                    className="w-48 h-48 bg-white/60 rounded-full shadow-inner mx-auto bg-cover bg-center"
                    style={{ backgroundImage: "url('/cloud.png')" }}
                  />
                </div>
              </div>

              <div className="mt-10">
                <h3 className="text-2xl mb-2">Coordenadas</h3>
                <p className="text-lg">
                  Latitude {weather.coordinates.lat}, Longitude {weather.coordinates.lon}
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
