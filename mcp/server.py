from mcp.server.fastmcp import FastMCP
from trip_client import TripClient
from tools import trips, places, categories, planning, search
import logging
from typing import Optional, List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP and TripClient
mcp = FastMCP("Trip")
client = TripClient()

# --- Trip Tools ---
@mcp.tool()
async def list_trips() -> List[Dict]:
    """List all user trips."""
    return await trips.list_trips(client)

@mcp.tool()
async def get_trip(trip_id: int) -> Dict:
    """Get detailed information about a specific trip."""
    return await trips.get_trip(client, trip_id)

@mcp.tool()
async def create_trip(name: str, currency: str = "€") -> Dict:
    """Create a new trip."""
    return await trips.create_trip(client, name, currency)

@mcp.tool()
async def update_trip(trip_id: int, name: Optional[str] = None, archived: Optional[bool] = None, notes: Optional[str] = None) -> Dict:
    """Update trip details."""
    kwargs = {k: v for k, v in {"name": name, "archived": archived, "notes": notes}.items() if v is not None}
    return await trips.update_trip(client, trip_id, **kwargs)

@mcp.tool()
async def delete_trip(trip_id: int) -> str:
    """Delete a trip."""
    await trips.delete_trip(client, trip_id)
    return f"Trip {trip_id} deleted."

# --- Place Tools ---
@mcp.tool()
async def list_places() -> List[Dict]:
    """List all saved places."""
    return await places.list_places(client)

@mcp.tool()
async def get_place(place_id: int) -> Dict:
    """Get detailed information about a specific place."""
    return await places.get_place(client, place_id)

@mcp.tool()
async def create_place(
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
    return await places.create_place(client, name, lat, lng, place, category_id, description, price, duration)

# --- Category Tools ---
@mcp.tool()
async def list_categories() -> List[Dict]:
    """List all place categories."""
    return await categories.list_categories(client)

# --- Planning Tools ---
@mcp.tool()
async def add_trip_day(trip_id: int, label: str, dt: Optional[str] = None) -> Dict:
    """Add a day to a trip. dt should be in YYYY-MM-DD format."""
    return await planning.add_trip_day(client, trip_id, label, dt)

@mcp.tool()
async def add_trip_item(
    trip_id: int, 
    day_id: int, 
    time: str, 
    text: str, 
    comment: Optional[str] = None,
    place_id: Optional[int] = None,
    price: Optional[float] = None,
    status: Optional[str] = None
) -> Dict:
    """Add an itinerary item to a trip day. time should be HH:MM."""
    return await planning.add_trip_item(client, trip_id, day_id, time, text, comment, place_id, price, status)

@mcp.tool()
async def get_packing_list(trip_id: int) -> List[Dict]:
    """Get the packing list for a trip."""
    return await planning.get_packing_list(client, trip_id)

@mcp.tool()
async def add_packing_item(trip_id: int, text: str, category: str, qt: int = 1) -> Dict:
    """Add an item to the packing list. Categories: clothes, toiletries, tech, documents, other."""
    return await planning.add_packing_item(client, trip_id, text, category, qt)

@mcp.tool()
async def get_checklist(trip_id: int) -> List[Dict]:
    """Get the checklist for a trip."""
    return await planning.get_checklist(client, trip_id)

@mcp.tool()
async def add_checklist_item(trip_id: int, text: str) -> Dict:
    """Add an item to the trip checklist."""
    return await planning.add_checklist_item(client, trip_id, text)

# --- Search Tools ---
@mcp.tool()
async def search_places(q: str) -> List[Dict]:
    """Search for places using the configured provider (OSM or Google)."""
    return await search.search_places(client, q)

@mcp.tool()
async def geocode(q: str) -> Dict:
    """Geocode a location name to get coordinates."""
    return await search.geocode(client, q)

if __name__ == "__main__":
    mcp.run()
