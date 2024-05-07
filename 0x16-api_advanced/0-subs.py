#!/usr/bin/python3
"""Queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
"""
import requests


def number_of_subscribers(subreddit):
    """Gets the total subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Subs/0.1"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
