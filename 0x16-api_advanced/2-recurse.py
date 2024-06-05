#!/usr/bin/python3
"""Recursive function
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """A function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit"""
    if after is None and count != 0:
        return hot_list
    if after is not None:
        url = "https://www.reddit.com/r/{}/.json?after={}".format(
            subreddit, after
            )
    else:
        url = "https://www.reddit.com/r/{}/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 100
    }
    with requests.get(url, headers=headers, params=params,
                      allow_redirects=False) as resp:
        if resp.status_code != 200 and count == 0:
            return None
        if resp.status_code != 200 and count != 0:
            return hot_list
        results = resp.json().get("data")
        for result in results.get('children'):
            data = result.get('data')
            hot_list.append(data.get('title'))
        count += len(results.get('children'))
        after = results.get('after')
        return recurse(subreddit, hot_list, after, count)
