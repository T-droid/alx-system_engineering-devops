#!/usr/bin/python3
"""function to query reddit api and return number of subscribers"""
def number_of_subscribers(subreddit):
    """function to get number of subreddi subscribers"""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers={'User-Agent': 'your-app-name'})
    if response.status_code == 200:
        sub_info = response.json()['data']
        return(sub_info['subscribers'])