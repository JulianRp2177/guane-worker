from datetime import datetime

from httpx._models import Response

from app.logging import get_logging

logger = get_logging(__name__)


class Responses:
    def __init__(self):
        self.code_switcher = {
            400: self.__400,
            401: self.__401,
            403: self.__403,
            404: self.__404,
            422: self.__422,
            500: self.__500,
        }

    def __400(self):
        return f"{datetime.now()}: Bad request"

    def __401(self):
        return f"{datetime.now()}: Not authorizated"

    def __403(self):
        return f"{datetime.now()}: Method not allowed"

    def __404(self):
        return f"{datetime.now()}: Not found"

    def __422(self):
        return f"{datetime.now()}: Unprocessable Entity"

    def __500(self):
        return f"{datetime.now()}: Internal server error"

    async def check_codes(self, *, response: Response, delete_method=False):
        code = self.code_switcher.get(response.status_code, lambda: None)
        content = code()
        if content:
            logger.error(
                f"{datetime.now()} - {(response.json().get('detail', None)) if not delete_method else response.reason_phrase}"
            )
            raise Exception(content)
