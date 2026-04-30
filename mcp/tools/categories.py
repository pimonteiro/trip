from typing import List, Dict
from trip_client import TripClient

async def list_categories(client: TripClient) -> List[Dict]:
    """List all place categories."""
    return await client.get("/api/categories")

async def create_category(client: TripClient, name: str, color: str = "#000000") -> Dict:
    """Create a new place category."""
    return await client.post("/api/categories", json={"name": name, "color": color})

async def update_category(client: TripClient, category_id: int, **kwargs) -> Dict:
    """Update a place category."""
    return await client.put(f"/api/categories/{category_id}", json=kwargs)

async def delete_category(client: TripClient, category_id: int) -> None:
    """Delete a place category (and its associated places)."""
    await client.delete(f"/api/categories/{category_id}")
