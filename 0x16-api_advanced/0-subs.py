#!/usr/bin/python3
"""module - function_name number_of subscribers
 """
import requests

def number_of_subscribers(subreddit):
    """A function to determine the number of subscribers
    to a subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; \
        Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0'
    }
    with requests.get(url, headers=headers) as resp:
        if resp.status_code != 200:
            return 0
        else:
            resp_data = resp.json()['data']
            number_of_subscribers = resp_data.get('subscribers')
            return number_of_subscribers
