from moviebox_api.v3 import MovieBoxHttpClient
from moviebox_api.v3.core import ItemDetails


async def get_details(subject_id: str):
    async with MovieBoxHttpClient() as client:
        details = ItemDetails(
            client_session=client,
            include_seasons=True,
        )

        return await details.get_content(subject_id)