#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/UnresolvedMysteries/hot.json"
    headers = {"User-Agent": "python:subreddit.recurse:v1.0 (by /u/yourusername)"}
    params = {"limit": 100, "after": after}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            for post in children:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None
