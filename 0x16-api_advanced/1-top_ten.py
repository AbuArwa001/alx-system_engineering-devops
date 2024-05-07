#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Gets the total subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Subs/0.1"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        titles = data["data"]["children"]
        i = 0
        for title in titles:
            if "title" in title["data"]:
                print(title["data"]["title"])
                i = i + 1
            if i == 10:
                break
    else:
        print(None)
