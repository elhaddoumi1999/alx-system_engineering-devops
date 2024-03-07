import requests

def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    Return 0 if an invalid subreddit is given.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a proper user agent to avoid being blocked by Reddit
    headers = {'User-Agent': 'My User Agent 1.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
