from typing import Optional, List, Dict
from trip_client import TripClient

async def list_places(client: TripClient) -> List[Dict]:
    """List all saved places."""
    return await client.get("/api/places")

async def get_place(client: TripClient, place_id: int) -> Dict:
    """Get detailed information about a specific place."""
    return await client.get(f"/api/places/{place_id}")

async def create_place(
    client: TripClient, 
    name: str, 
    lat: float, 
    lng: float, 
    place: str, 
    category_id: int,
    description: Optional[str] = None,
    price: Optional[float] = None,
    duration: Optional[int] = None
) -> Dict:
    """Create a new saved place."""
    payload = {
        "name": name,
        "lat": lat,
        "lng": lng,
        "place": place,
        "category_id": category_id,
        "description": description,
        "price": price,
        "duration": duration
    }
    return await client.post("/api/places", json=payload)

async def update_place(client: TripClient, place_id: int, **kwargs) -> Dict:
    """Update details of a saved place."""
    return await client.put(f"/api/places/{place_id}", json=kwargs)

async def delete_place(client: TripClient, place_id: int) -> None:
    """Delete a saved place."""
    await client.delete(f"/api/places/{place_id}")
