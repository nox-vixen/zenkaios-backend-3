from moviebox_api.v3.core import Homepage
from .client import client


async def get_home():
    home = Homepage(client)
    return await home.get_content()