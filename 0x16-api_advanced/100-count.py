import requests
import re


def count_words(subreddit, word_list, counts={}, after=""):
    """
    Recursively fetches titles of hot articles from a
    subreddit and counts occurrences of specified keywords.
    """
    # Initialize the count dictionary during the first call
    if not counts:
        counts = {word.lower(): 0 for word in word_list}

    # Base URL for fetching hot posts in a subreddit
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)

    # Append 'after' parameter for pagination
    if after:
        url += "&after={}".format(after)

    # Set up headers to include a custom User-Agent
    headers = {"User-Agent": "reddit:word_count:v1.0 (by /u/khalfanathman)"}

    # Make the HTTP request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        after = data.get("data", {}).get("after", None)

        # Process each post title
        for post in posts:
            title = post["data"]["title"].lower()
            for word in counts.keys():
                # Count occurrences of each keyword in the title
                counts[word] += len(
                    re.findall(r"\b{}\b".format(re.escape(word)), title)
                )
        if after:
            return count_words(subreddit, word_list, counts, after)
        else:
            filtered_counts = {
                word: count for word, count in counts.items() if count > 0
            }
            for word in sorted(
                filtered_counts, key=lambda k: (-filtered_counts[k], k)
            ):
                print("{}: {}".format(word, filtered_counts[word]))
    elif not after:
        return
