"""@subreddit: the subreddit to get the posts from
    """
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    headers = {"User-Agent": "0x16. API advanced by Cu7ious"}
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code is not 200:
