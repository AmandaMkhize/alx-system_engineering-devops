#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers (not active
users, total subscribers) for a given subreddit. If an invalid subreddit
is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API"""
    headers = {
        "User-Agent": "0x16. API_advanced-e_kiminza"
    }
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code != 200:
            return 0

        data = response.json().get("data", {})
        subscribers = data.get("subscribers", 0)
        return subscribers

    except requests.RequestException:
        return 0
    except ValueError:
        return 0


if __name__ == "__main__":
    subreddit = "python"
    print(number_of_subscribers(subreddit))
