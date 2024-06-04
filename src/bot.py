import tweepy
import requests
import time
from datetime import datetime

# Repository owner and name
REPO_OWNER = 'Ryun1'
REPO_NAME = 'test-temp-repo'

# Twitter API credentials
TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET_KEY = 'your_twitter_api_secret_key'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'

# GitHub API credentials
GITHUB_TOKEN = 'your_github_token'
REPO_OWNER = 'repository_owner'
REPO_NAME = 'repository_name'

# Initialize Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Track the latest PR seen
latest_pr_id = None

def get_latest_pr():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)
    pr_list = response.json()
    if pr_list:
        return pr_list[0]  # Return the most recent PR
    return None

def tweet_new_pr(pr):
    pr_title = pr['title']
    pr_url = pr['html_url']
    pr_creator = pr['user']['login']
    tweet = f"New PR created by @{pr_creator}: {pr_title} {pr_url}"
    api.update_status(tweet)

while True:
    latest_pr = get_latest_pr()
    if latest_pr and (latest_pr_id is None or latest_pr['id'] != latest_pr_id):
        latest_pr_id = latest_pr['id']
        tweet_new_pr(latest_pr)
    time.sleep(60)  # Wait for 1 minute before checking again