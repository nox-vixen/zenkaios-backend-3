from moviebox_api.v3 import Homepage, MovieBoxHttpClient


async def get_home():
    async with MovieBoxHttpClient() as client:

        home = Homepage(client)
        data = await home.get_content()

        hero = []
        sections = []

        # Parse every homepage block
        for key, block in data.items():

            if not isinstance(block, dict):
                continue

            # Hero Banner
            if block.get("type") == "BANNER":
                banners = block.get("banner", {}).get("banners", [])

                for banner in banners:
                    subject = banner.get("subject", {})

                    hero.append({
                        "id": subject.get("subjectId"),
                        "title": subject.get("title"),
                        "image": banner.get("image", {}).get("url"),
                        "cover": subject.get("cover", {}).get("url"),
                        "year": subject.get("releaseDate"),
                        "type": subject.get("subjectType"),
                    })

            # Horizontal sections
            elif block.get("subjects"):

                items = []

                for subject in block.get("subjects", []):

                    items.append({
                        "id": subject.get("subjectId"),
                        "title": subject.get("title"),
                        "image": subject.get("cover", {}).get("url"),
                        "year": subject.get("releaseDate"),
                        "type": subject.get("subjectType"),
                    })

                sections.append({
                    "title": block.get("title"),
                    "items": items
                })

        return {
            "hero": hero,
            "sections": sections
        }