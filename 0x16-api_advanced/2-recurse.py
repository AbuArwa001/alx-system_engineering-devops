#!/usr/bin/python3
"""
 Recursively fetches titles of all hot articles from a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Recursively fetches titles of all hot articles from a subreddit.
    Returns a list of titles, or None if the subreddit is invalid.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {'User-Agent': 'script:scr ipt:v1.0 (by /u/yourusername)'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after', None)
        for post in posts:
            hot_list.append(post['data']['title'])
        if not after:
            return hot_list if hot_list else None
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
