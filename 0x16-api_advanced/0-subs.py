#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys

def number_of_subscribers(subreddit):
    """Read Reddit API and return number of subscribers"""
    headers = {'User-Agent': '/u/ledbag123 API Python for Holberton School'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
