from typing import Optional, List, Dict
from trip_client import TripClient

async def search_places(client: TripClient, q: str) -> List[Dict]:
    """Search for places using the configured provider (OSM or Google)."""
    return await client.get("/api/completions/search", params={"q": q})

async def nearby_search(client: TripClient, latitude: float, longitude: float) -> List[Dict]:
    """Search for nearby places."""
    return await client.post("/api/completions/nearby", json={"latitude": latitude, "longitude": longitude})

async def geocode(client: TripClient, q: str) -> Dict:
    """Geocode a location name to get bounding box coordinates."""
    return await client.get("/api/completions/geocode", params={"q": q})

async def get_route(client: TripClient, coordinates: List[Dict], profile: str = "driving") -> Dict:
    """Get a route between multiple coordinates.
    coordinates should be a list of {'lat': float, 'lng': float}
    profile can be 'driving', 'walking', 'cycling'
    """
    return await client.post("/api/completions/route", json={"coordinates": coordinates, "profile": profile})
