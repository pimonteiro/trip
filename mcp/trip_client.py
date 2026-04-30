import os
import httpx
from typing import Any, Dict, Optional
import logging
from datetime import datetime, UTC

logger = logging.getLogger(__name__)

class TripClient:
    def __init__(self):
        self.base_url = os.getenv("TRIP_URL", "").rstrip("/")
        self.username = os.getenv("TRIP_USERNAME")
        self.password = os.getenv("TRIP_PASSWORD")
        
        if not all([self.base_url, self.username, self.password]):
            raise ValueError("TRIP_URL, TRIP_USERNAME, and TRIP_PASSWORD must be set in environment")
        
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self.client = httpx.AsyncClient(base_url=self.base_url)

    async def login(self):
        logger.info(f"Logging in to {self.base_url} as {self.username}")
        response = await self.client.post(
            "/api/auth/login",
            json={"username": self.username, "password": self.password}
        )
        response.raise_for_status()
        data = response.json()
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]
        logger.info("Successfully logged in")

    async def _refresh_access_token(self):
        if not self.refresh_token:
            await self.login()
            return

        logger.info("Refreshing access token")
        try:
            response = await self.client.post(
                "/api/auth/refresh",
                json={"refresh_token": self.refresh_token}
            )
            response.raise_for_status()
            data = response.json()
            self.access_token = data["access_token"]
            logger.info("Successfully refreshed access token")
        except Exception as e:
            logger.error(f"Failed to refresh token: {e}. Attempting full login.")
            await self.login()

    async def request(self, method: str, path: str, **kwargs) -> Any:
        if not self.access_token:
            await self.login()

        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {self.access_token}"
        kwargs["headers"] = headers

        try:
            response = await self.client.request(method, path, **kwargs)
            if response.status_code == 401:
                await self._refresh_access_token()
                headers["Authorization"] = f"Bearer {self.access_token}"
                response = await self.client.request(method, path, **kwargs)
            
            response.raise_for_status()
            return response.json() if response.content else None
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error {e.response.status_code} for {method} {path}: {e.response.text}")
            raise

    async def get(self, path: str, params: Optional[Dict] = None) -> Any:
        return await self.request("GET", path, params=params)

    async def post(self, path: str, json: Optional[Dict] = None) -> Any:
        return await self.request("POST", path, json=json)

    async def put(self, path: str, json: Optional[Dict] = None) -> Any:
        return await self.request("PUT", path, json=json)

    async def delete(self, path: str) -> Any:
        return await self.request("DELETE", path)

    async def close(self):
        await self.client.aclose()
