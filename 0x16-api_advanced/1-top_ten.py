#!/usr/bin/python3
"""
prints the titles of top 10 hot posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    prints titles of the 10 hottest posts on a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Linux:0x16-api_advanced"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
