#!/usr/bin/python3
#ulala

import requests


def top_ten(subreddit):
    #aheee
    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if r.status_code == 200:
        for c in r.json().get("data").get("children"):
            d = c.get("data")
            t = d.get("title")
            print(t)
    else:
        print(None)
