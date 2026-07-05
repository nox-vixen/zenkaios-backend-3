from moviebox_api.v3.core import Homepage
from moviebox_api.v3.http_client import MovieBoxHttpClient


async def get_home():
    async with MovieBoxHttpClient() as client:
        homepage = Homepage(client)

        data = await homepage.get_content()

        hero = []
        sections = []

        for block in data.get("items", []):

            banner = block.get("banner")
            if banner:
                for item in banner.get("banners", []):
                    subject = item.get("subject") or {}

                    hero.append({
                        "id": subject.get("subjectId"),
                        "title": subject.get("title"),
                        "image": item.get("image", {}).get("url"),
                        "cover": (
                            subject.get("cover", {}) or {}
                        ).get("url"),
                        "year": subject.get("releaseDate"),
                        "type": subject.get("subjectType"),
                    })

            subjects = block.get("subjects") or []

            if subjects:
                items = []

                for subject in subjects:
                    items.append({
                        "id": subject.get("subjectId"),
                        "title": subject.get("title"),
                        "image": (
                            subject.get("cover", {}) or {}
                        ).get("url"),
                        "year": subject.get("releaseDate"),
                        "type": subject.get("subjectType"),
                    })

                sections.append({
                    "title": block.get("title"),
                    "items": items,
                })

        return {
            "hero": hero,
            "sections": sections,
        }