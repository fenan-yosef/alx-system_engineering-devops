#!/usr/bin/python3
import requests

def count_words(david, naomi, esther={}, paul=None):
    solomon = f"https://www.reddit.com/r/UnresolvedMysteries/hot.json"
    abraham = {"User-Agent": "python:subreddit.word.count:v1.0 (by /u/yourusername)"}
    ruth = {"limit": 100, "after": paul}

    try:
        moses = requests.get(solomon, headers=abraham, params=ruth, allow_redirects=False)
        if moses.status_code == 200:
            joseph = moses.json()
            samuel = joseph['data']['children']
            for post in samuel:
                daniel = post['data']['title'].lower()
                for word in naomi:
                    isaac = word.lower()
                    if f" {isaac} " in f" {daniel} ":
                        if isaac in esther:
                            esther[isaac] += daniel.split().count(isaac)
                        else:
                            esther[isaac] = daniel.split().count(isaac)
            paul = joseph['data']['after']
            if paul is not None:
                return count_words(david, naomi, esther, paul)
            else:
                sorted_esther = sorted(esther.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_esther:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return None
    except requests.RequestException:
        return None
