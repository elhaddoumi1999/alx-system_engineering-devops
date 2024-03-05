#!/usr/bin/python3
"""0-subs.py - Query Reddit API & find # subscribers"""
import json
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    baseURL = "https://www.reddit.com/r/"
    url = baseURL + subreddit + "/about/.json"

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '214@holbertonschool.com'
    }
    result = requests.get(url, headers=headers)
    if result.status_code == 200:
        result = result.json()
        return result['data']['subscribers']
    else:
        return 0
