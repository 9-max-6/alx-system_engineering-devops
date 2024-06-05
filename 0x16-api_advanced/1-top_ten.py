#!/usr/bin/python3
"""module - exploring the reddit api
"""
import requests


def top_ten(subreddit):
    """A function to display the titles of the
    first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    with requests.get(url, headers=headers, params=params,
                      allow_redirects=False) as resp:
        if resp.status_code == 404:
            print("None")
            return
        results = resp.json().get("data")
        for result in results.get('children'):
            data = result.get('data')
            print(data.get('title'))
