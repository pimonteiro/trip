# Trip MCP Server

Model Context Protocol (MCP) server for the Trip application. This server allows LLMs to manage trips, itinerary items, packing lists, and search for places.

## Setup

### Prerequisites

- Python 3.10+
- `uv` package manager (recommended)

### Environment Variables

The server requires the following environment variables to authenticate with your Trip instance:

- `TRIP_URL`: The base URL of your Trip instance (e.g., `http://localhost:8000`)
- `TRIP_USERNAME`: Your login username
- `TRIP_PASSWORD`: Your login password

## Usage

### Using with Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "trip": {
      "command": "uv",
      "args": [
        "run",
        "--directory", "/home/lazypad/Documents/repos/trip/mcp",
        "server.py"
      ],
      "env": {
        "TRIP_URL": "YOUR_TRIP_URL",
        "TRIP_USERNAME": "YOUR_USERNAME",
        "TRIP_PASSWORD": "YOUR_PASSWORD"
      }
    }
  }
}
```

### Development and Testing

You can test the server using the MCP Inspector:

```bash
uv run mcp dev server.py
```

## Available Tools

- `list_trips`: List all user trips.
- `get_trip`: Get detailed information about a trip.
- `create_trip`: Create a new trip.
- `update_trip`: Update trip details.
- `delete_trip`: Delete a trip.
- `list_places`: List saved places.
- `get_place`: Get place details.
- `create_place`: Save a new place.
- `list_categories`: List place categories.
- `add_trip_day`: Add a day to a trip.
- `add_trip_item`: Add an itinerary item (time, text, place).
- `get_packing_list`: Get packing items for a trip.
- `add_packing_item`: Add to the packing list.
- `get_checklist`: Get trip checklist.
- `add_checklist_item`: Add to the checklist.
- `search_places`: Search for places using OSM/Google.
- `geocode`: Get coordinates for a location name.
