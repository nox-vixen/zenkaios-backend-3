from moviebox_api.v3.http_client import MovieBoxHttpClient
from moviebox_api.v3.core import Homepage


async def get_home():
    async with MovieBoxHttpClient() as client:
        home = Homepage(client)
        data = await home.get_content()

        return {
            "first_item": data["items"][0],
            "second_item": data["items"][1]
        }