#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after="", word_count={}):
    """Counts the occurrences of each word in `word_list` in the titles of hot articles."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data", {})
        after = data.get("after")
        posts = data.get("children", [])
        
        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            for word in word_list:
                word_lower = word.lower()
                count = title.split().count(word_lower)
                if count > 0:
                    if word_lower in word_count:
                        word_count[word_lower] += count
                    else:
                        word_count[word_lower] = count
        
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            if word_count:
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")
            return
    else:
        return
