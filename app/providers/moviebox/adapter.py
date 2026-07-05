def normalize_home(data: dict):
    result = {
        "hero": [],
        "sections": []
    }

    items = data.get("items", [])

    for item in items:
        item_type = item.get("type")

        if item_type == "BANNER":
            for subject in item.get("subjects", []):
                result["hero"].append({
                    "id": subject.get("subjectId"),
                    "title": subject.get("title"),
                    "poster": subject.get("image"),
                    "backdrop": subject.get("banner"),
                    "type": subject.get("subjectType")
                })

        elif item_type == "LIST":
            cards = []

            for subject in item.get("subjects", []):
                cards.append({
                    "id": subject.get("subjectId"),
                    "title": subject.get("title"),
                    "poster": subject.get("image"),
                    "type": subject.get("subjectType")
                })

            result["sections"].append({
                "title": item.get("title"),
                "items": cards
            })

    return result