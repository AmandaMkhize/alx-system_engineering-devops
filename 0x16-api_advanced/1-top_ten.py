#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    try:
        # Send a GET request to the subreddit's hot posts page
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if the response status code is 200 (OK)
        response.raise_for_status()

        # Parse the JSON response and extract the 'data' section
        data = response.json()

        # Check if 'data' key exists in the response JSON
        if "data" in data and "children" in data["data"]:
            children = data["data"]["children"]
            # Print the titles of the top 10 hottest posts
            for child in children:
                print(child["data"]["title"])
        else:
            print("No posts found.")
    
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)

