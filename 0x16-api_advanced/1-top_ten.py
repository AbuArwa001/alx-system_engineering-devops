#!/usr/bin/python3
import requests
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts of a given subreddit.
    """
    # Reddit API URL for hot posts in a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'python:requests (by /u/khalfanathman)'}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(None)
        else:
            for post in posts:
                print(post['data']['title'])
    else:
        print(None)
