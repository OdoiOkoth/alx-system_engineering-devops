def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    headers = {
        "User-Agent": "0x16. API_advanced-e_kiminza"
        }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
