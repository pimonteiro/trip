from typing import Optional, List, Dict
from trip_client import TripClient

async def list_trips(client: TripClient) -> List[Dict]:
    """List all user trips."""
    return await client.get("/api/trips")

async def get_trip(client: TripClient, trip_id: int) -> Dict:
    """Get detailed information about a specific trip."""
    return await client.get(f"/api/trips/{trip_id}")

async def create_trip(client: TripClient, name: str, currency: str = "€") -> Dict:
    """Create a new trip."""
    return await client.post("/api/trips", json={"name": name, "currency": currency})

async def update_trip(client: TripClient, trip_id: int, **kwargs) -> Dict:
    """Update trip details (name, currency, notes, archived)."""
    return await client.put(f"/api/trips/{trip_id}", json=kwargs)

async def delete_trip(client: TripClient, trip_id: int) -> None:
    """Delete a trip."""
    await client.delete(f"/api/trips/{trip_id}")

async def get_trip_balance(client: TripClient, trip_id: int) -> Dict:
    """Get the expense balance for a trip."""
    return await client.get(f"/api/trips/{trip_id}/balance")
