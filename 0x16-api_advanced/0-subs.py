#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data['data']['subscribers']
