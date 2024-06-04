#!/usr/bin/python3
"""
tsegur betam des mil neger new
"""

import requests


def number_of_subscribers(subreddit):
    r = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0
