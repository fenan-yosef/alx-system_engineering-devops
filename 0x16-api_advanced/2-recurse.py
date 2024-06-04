#!/usr/bin/python3
"""
My name is fenan
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    hello
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if response.status_code == 200:
        for child in response.json().get("data").get("children"):
            post_data = child.get("data")
            title = post_data.get("title")
            hot_list.append(title)
        next_page = response.json().get("data").get("after")

        if next_page is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, next_page)
    else:
        return None
