#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
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
            return hot_list if hot_list else None
        elif response.status_code in [301, 302, 404]:  # Handling redirects and not found
            return None
        else:
            return None
    except requests.RequestException:
        return None

# Example usage:
# hot_posts = recurse('programming')
# print(hot_posts)