from tavily import TavilyClient

client = TavilyClient("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")

def find_youtube_link(title: str):

    query = f"""
    הרב שמואל סעדון {title} youtube
    """

    results = client.search(
        query=query,
        search_depth="basic",
        max_results=5
    )

    for result in results["results"]:

        url = result["url"]

        if "youtube.com" in url or "youtu.be" in url:
            return url

    return ""