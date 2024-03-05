#!/usr/bin/python3
"""1-top_ten.py - Query Reddit API & find Top10 subreddits hot posts"""
import json
import requests


def top_ten(subreddit):
    """Return Top10 subreddit hot posts"""
    baseURL = "https://www.reddit.com/r/"
    url = baseURL + subreddit + "/hot/.json?limit=10"
    # https://www.reddit.com/r/programming/hot/.json&limit=10

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '214@holbertonschool.com'
    }
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        result = result.json()
        children = result.get('data').get('children')
        for i in range(10):
            # print("{}".format(result['data']['children'][i]['data']['title']))
            title = children[i].get('data').get('title')
            print("{}".format(title))
    else:
        print("None")
