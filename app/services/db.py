from typing import Any, Dict

from app.config import settings
from app.infra.httpx.client import HTTPXClient
from app.services.responses import Responses


class ReservationService:
    def __init__(
        self,
        url: str,
        check_codes: Responses = Responses(),
        client: HTTPXClient = HTTPXClient(),
    ):
        self.url = url
        self._client = client
        self._check_codes = check_codes

    async def create_reservation(self, payload: dict) -> Dict[str, Any]:
        print(self.url)
        response = await self._client.post(url_service=f"{self.url}", body=payload,  timeout=800)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response


reservation_service = ReservationService(url=f"{settings.DB_API}/api/user/reservation")
