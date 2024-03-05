#!/usr/bin/python3
"""100-count.py - Query Reddit API & count unique words
in titles of hot articles using recursion"""
import json
import requests


def count_words(subreddit, word_list, params={}):
    """Sort hot subreddit article titles using recursion"""
    d = {k: 0 for k in word_list}
    nWords = len(d)
    payload = {}

    baseURL = "https://www.reddit.com/r/"
    url = baseURL + subreddit + "/hot/.json?limit=100"

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '214 at Holberton'
    }
    result = requests.get(url, headers=headers, params=params)
    title = []
    if result.status_code == 200:

        result = result.json()
        children = result.get('data').get('children')
        for i in range(len(children)):
            t = children[i].get('data').get('title').split()
        print("title:{}".format(t))
        after = result.get('data').get('after')
        if after is None:
            return None
        else:
            payload = {"after": after, "d": d}
            count_words(subreddit, word_list, payload)
            return None
    else:
        return None
