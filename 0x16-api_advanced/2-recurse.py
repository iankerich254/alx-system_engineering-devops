#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data", {})
        after = data.get("after")
        posts = data.get("children", [])
        
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))
        
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
