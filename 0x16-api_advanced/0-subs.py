#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers (not active
users, total subscribers) for a given subreddit. If an invalid subreddit
is given, the function should return 0.
"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API for the number of subscribers of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python requests"  # Replace with your own User-Agent
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get("data", {})
            subscribers = data.get("subscribers", 0)
            return subscribers
        else:
            return 0
        
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 0
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))

