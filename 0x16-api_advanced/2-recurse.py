import requests

def recurse(subreddit, hot_list=[], after=None, recursion_depth=0, max_depth=10):
    if recursion_depth > max_depth:
        print(f"Max recursion depth {max_depth} reached.")
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": f"python:subreddit.recurse:v1.0 (by /u/yourusername)"}
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
                return recurse(subreddit, hot_list, after, recursion_depth + 1, max_depth)
            return hot_list
        else:
            print(f"Failed to fetch data: Status code {response.status_code}")
            return hot_list
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return hot_list