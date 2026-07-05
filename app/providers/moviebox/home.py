from moviebox_api.v3.http_client import MovieBoxHttpClient
from moviebox_api.v3.core import Homepage

from .adapter import normalize_home


async def get_home():
    async with MovieBoxHttpClient() as client:
        home = Homepage(client)
        data = await home.get_content()
        return normalize_home(data)