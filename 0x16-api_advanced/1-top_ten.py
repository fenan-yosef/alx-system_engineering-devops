#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/UnresolvedMysteries/hot.json?limit=10"
    headers = {"User-Agent": "python:subreddit.top.ten:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")
    except requests.RequestException:
        print("None")
