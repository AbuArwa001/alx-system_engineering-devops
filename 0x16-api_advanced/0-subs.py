#!/usr/bin/python3
"""Queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Script/0.0.1"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

# Example usage
if __name__ == '__main__':
    subreddit = "programming"
    print(number_of_subscribers(subreddit))
