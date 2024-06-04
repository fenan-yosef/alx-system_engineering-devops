#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    #THIS CODE RETURN TOP TEN SUBSCRIBERS OF REDDIT
    alx_redditUrl = f"https://www.reddit.com/r/UnresolvedMysteries/about.json"
    yRED = {"User-Agent": "python:subreddit.subscriber.count:v1.0 (by /u/yourusername)"}
    try:
        response = requests.get(alx_redditUrl, headers=yRED, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0
