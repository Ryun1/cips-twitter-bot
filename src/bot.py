import tweepy
import requests
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Twitter API credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

print(TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_TOKEN_SECRET,TWITTER_API_KEY,TWITTER_API_SECRET_KEY)

# GitHub API credentials
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER =os.getenv('REPO_OWNER')
REPO_NAME = os.getenv('REPO_NAME')

print(GITHUB_TOKEN,REPO_NAME,REPO_OWNER)

# Initialize Twitter API
# auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
# auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

client = tweepy.Client(consumer_key=TWITTER_API_KEY, consumer_secret=TWITTER_API_SECRET_KEY,access_token=TWITTER_ACCESS_TOKEN, access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

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

    try:
        # api.update_status(status=tweet)
        client.create_tweet(text=tweet)
    except tweepy.errors.TweepyException as e:
        print(e)
   
    

while True:
    latest_pr = get_latest_pr()
    if latest_pr and (latest_pr_id is None or latest_pr['id'] != latest_pr_id):
        latest_pr_id = latest_pr['id']
        tweet_new_pr(latest_pr)
    time.sleep(60)  # Wait for 1 minute before checking again
