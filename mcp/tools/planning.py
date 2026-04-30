from typing import Optional, List, Dict
from trip_client import TripClient

# Trip Days
async def add_trip_day(client: TripClient, trip_id: int, label: str, dt: Optional[str] = None) -> Dict:
    """Add a day to a trip."""
    return await client.post(f"/api/trips/{trip_id}/days", json={"label": label, "dt": dt})

async def update_trip_day(client: TripClient, trip_id: int, day_id: int, **kwargs) -> Dict:
    """Update a trip day (label, date, notes)."""
    return await client.put(f"/api/trips/{trip_id}/days/{day_id}", json=kwargs)

async def delete_trip_day(client: TripClient, trip_id: int, day_id: int) -> None:
    """Delete a trip day."""
    await client.delete(f"/api/trips/{trip_id}/days/{day_id}")

# Trip Items
async def add_trip_item(
    client: TripClient, 
    trip_id: int, 
    day_id: int, 
    time: str, 
    text: str, 
    comment: Optional[str] = None,
    place_id: Optional[int] = None,
    price: Optional[float] = None,
    status: Optional[str] = None
) -> Dict:
    """Add an itinerary item to a trip day."""
    payload = {
        "time": time,
        "text": text,
        "comment": comment,
        "place": place_id,
        "price": price,
        "status": status
    }
    return await client.post(f"/api/trips/{trip_id}/days/{day_id}/items", json=payload)

async def update_trip_item(client: TripClient, trip_id: int, day_id: int, item_id: int, **kwargs) -> Dict:
    """Update an itinerary item."""
    return await client.put(f"/api/trips/{trip_id}/days/{day_id}/items/{item_id}", json=kwargs)

async def delete_trip_item(client: TripClient, trip_id: int, day_id: int, item_id: int) -> None:
    """Delete an itinerary item."""
    await client.delete(f"/api/trips/{trip_id}/days/{day_id}/items/{item_id}")

# Packing List
async def get_packing_list(client: TripClient, trip_id: int) -> List[Dict]:
    """Get the packing list for a trip."""
    return await client.get(f"/api/trips/{trip_id}/packing")

async def add_packing_item(client: TripClient, trip_id: int, text: str, category: str, qt: int = 1) -> Dict:
    """Add an item to the packing list."""
    return await client.post(f"/api/trips/{trip_id}/packing", json={"text": text, "category": category, "qt": qt})

async def update_packing_item(client: TripClient, trip_id: int, p_id: int, **kwargs) -> Dict:
    """Update a packing list item (packed status, quantity, etc.)."""
    return await client.put(f"/api/trips/{trip_id}/packing/{p_id}", json=kwargs)

async def delete_packing_item(client: TripClient, trip_id: int, p_id: int) -> None:
    """Delete a packing list item."""
    await client.delete(f"/api/trips/{trip_id}/packing/{p_id}")

# Checklist
async def get_checklist(client: TripClient, trip_id: int) -> List[Dict]:
    """Get the checklist for a trip."""
    return await client.get(f"/api/trips/{trip_id}/checklist")

async def add_checklist_item(client: TripClient, trip_id: int, text: str) -> Dict:
    """Add an item to the trip checklist."""
    return await client.post(f"/api/trips/{trip_id}/checklist", json={"text": text})

async def update_checklist_item(client: TripClient, trip_id: int, id: int, **kwargs) -> Dict:
    """Update a checklist item (checked status, text)."""
    return await client.put(f"/api/trips/{trip_id}/checklist/{id}", json=kwargs)

async def delete_checklist_item(client: TripClient, trip_id: int, id: int) -> None:
    """Delete a checklist item."""
    await client.delete(f"/api/trips/{trip_id}/checklist/{id}")
