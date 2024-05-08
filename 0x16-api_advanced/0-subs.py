#!/usr/bin/python3
"""Queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
"""
import requests


def number_of_subscribers(subreddit):
    """Gets the total subscribers for a given subreddit"""
    CLIENT_ID = "qp6arBsGNKBcbOfUDTVYeA"
    SECRET_KEY = "tAXMlRUvWxN5ITvL2YmkkWtLVq-b2g"
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    with open('pwd.txt', 'r') as f:
        pwd = f.read()
    data = {
        'grant_type': 'password',
        'username': 'Educational-Gear-868',
        'password': pwd
    }
    headers = {"User-Agent": "Subs/0.1"}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers['Authorization'] = 'beare {}'.format(TOKEN)
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
