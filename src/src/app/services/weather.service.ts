import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map } from 'rxjs';
import { DailyWeather } from '../types/trip';

@Injectable({
  providedIn: 'root'
})
export class WeatherService {
  constructor(private http: HttpClient) {}

  getForecast(lat: number, lng: number): Observable<DailyWeather[]> {
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lng}&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=auto&forecast_days=16`;
    return this.http.get<any>(url).pipe(
      map(response => {
        if (!response?.daily) return [];
        
        const daily = response.daily;
        const forecasts: DailyWeather[] = [];
        
        for (let i = 0; i < daily.time.length; i++) {
          const code = daily.weather_code[i];
          forecasts.push({
            date: daily.time[i],
            tempMax: Math.round(daily.temperature_2m_max[i]),
            tempMin: Math.round(daily.temperature_2m_min[i]),
            weatherCode: code,
            emoji: this.getEmoji(code),
            description: this.getDescription(code)
          });
        }
        
        return forecasts;
      })
    );
  }

  private getEmoji(code: number): string {
    if (code === 0) return '☀️';
    if (code === 1) return '🌤️';
    if (code === 2) return '⛅';
    if (code === 3) return '☁️';
    if (code === 45 || code === 48) return '🌫️'; // Fog
    if (code >= 51 && code <= 57) return '🌦️'; // Drizzle
    if (code >= 61 && code <= 67) return '🌧️'; // Rain
    if (code >= 80 && code <= 82) return '🌧️'; // Rain showers
    if ((code >= 71 && code <= 77) || (code >= 85 && code <= 86)) return '❄️'; // Snow
    if (code >= 95 && code <= 99) return '⛈️'; // Thunderstorm
    return '☁️';
  }

  private getDescription(code: number): string {
    if (code === 0) return 'Clear sky';
    if (code === 1) return 'Mainly clear';
    if (code === 2) return 'Partly cloudy';
    if (code === 3) return 'Overcast';
    if (code === 45 || code === 48) return 'Fog';
    if (code >= 51 && code <= 57) return 'Drizzle';
    if (code >= 61 && code <= 67) return 'Rain';
    if (code >= 71 && code <= 77) return 'Snow fall';
    if (code >= 80 && code <= 82) return 'Rain showers';
    if (code >= 85 && code <= 86) return 'Snow showers';
    if (code >= 95 && code <= 99) return 'Thunderstorm';
    return 'Unknown';
  }
}
