#!/usr/bin/python3
"""Print the titles of the first 10 hot posts listed by a subreddit"""

import requests

def top_ten(subreddit):
    """Print top ten hot titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}

    response = requests.get(url, headers={'User-Agent': 'your-app-name'}, params=params, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data", {}).get("children", [])
    
    if not results:
        print("No hot posts found")
        return
    
    [print(c.get("data", {}).get("title")) for c in results]