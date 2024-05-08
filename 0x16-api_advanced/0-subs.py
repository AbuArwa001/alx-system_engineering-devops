#!/usr/bin/python3
"""Queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
"""
import requests


def number_of_subscribers(subreddit):
    username = 'Educational-Gear-868'
    password = 'Educational-1001'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/Educational-Gear-868'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return (0)
