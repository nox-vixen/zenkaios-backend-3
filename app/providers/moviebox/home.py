from moviebox_api.v3.http_client import MovieBoxHttpClient
from moviebox_api.v3.core import Homepage


async def get_home():
    async with MovieBoxHttpClient() as client:
        home = Homepage(client)
        return await home.get_content()