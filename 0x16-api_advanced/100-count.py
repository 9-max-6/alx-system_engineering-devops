#!/usr/bin/python3
"""Recursive function
"""

import requests


def collapse_dictionary(a_dictionary):
    """A function to make unique a dict
    """
    the_keys = a_dictionary.keys()

    for key, value in a_dictionary.items():
        print(the_keys.count(key.lower()))
        value *= the_keys.count(key)


def set_dict(word_list, my_dict={}):
    """A function to make dict"""
    for word in word_list:
        my_dict[word.lower()] = 0
    return my_dict


def print_dict(a_dictionary):
    """A function to print a dictionary"""
    printed_keys = []
    for key, value in a_dictionary.items():
        if key not in printed_keys:
            print('{}: {}'.format(key, value))
            printed_keys.append(key)


def listing_count_words(a_listing, a_dictionary):
    """A function to count occurences of words in a title list
    for each word in a dictionary"""
    print(a_dictionary)
    for key, value in a_dictionary.items():
        count = 0
        for title in a_listing:
            insensitive_title = title.lower()
            insensitive_key = key.lower()
            for word in insensitive_title.split():
                if word == insensitive_key:
                    count += 1
        a_dictionary[key] += count
    print(a_dictionary)
    return a_dictionary



def count_words(subreddit, word_list, after=None, count=0, dict_count=None):
    """A function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit"""
    if after is None and count == 0:
        dict_count = set_dict(word_list)
    if after is not None and count > 100:
        return print_dict(dict_count)
    if after is not None and count != 0:
        url = "https://www.reddit.com/r/{}/.json?after={}".format(
            subreddit, after
            )
    else:
        url = "https://www.reddit.com/r/{}/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 25
    }
    new_listing = []
    with requests.get(url, headers=headers, params=params,
                      allow_redirects=False) as resp:
        if resp.status_code != 200 and count == 0:
            return dict_count
        if resp.status_code != 200 and count != 0:
            return
        results = resp.json().get("data")
        for result in results.get('children'):
            data = result.get('data')
            title = data.get('title')
            new_listing.append(title)
        new_dict_count = listing_count_words(new_listing, dict_count)
        count += len(results.get('children'))
        after = results.get('after')
        return count_words(subreddit, word_list, after, count, new_dict_count)
