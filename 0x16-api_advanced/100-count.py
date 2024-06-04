#!/usr/bin/python3
"""
Function to count words in all hot posts of a given Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursive function that queries the Reddit API, parses the title of all
        hot articles, and prints a sorted count of given keywords
    """
    # "All the world's a stage, and all the men and women merely players."
    if not word_list or word_list == [] or not subreddit:
        return

    # "This above all: to thine own self be true."
    u = f"https://www.reddit.com/r/{subreddit}/hot.json"
    h = {"User-Agent": "Mozilla/5.0"}

    p = {"limit": 100}
    if after:
        p["after"] = after

    r = requests.get(u, headers=h, params=p, allow_redirects=False)

    # "To be, or not to be, that is the question."
    if r.status_code != 200:
        return

    d = r.json()
    c = d["data"]["children"]

    for post in c:
        t = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in t:
                counts[word] = counts.get(word, 0) + t.count(word.lower())

    a = d["data"]["after"]
    if a:
        count_words(subreddit, word_list, a, counts)
    else:
        s_c = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in s_c:
            print(f"{word.lower()}: {count}")  # "Love all, trust a few, do wrong to none."
