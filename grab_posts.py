import praw
import random
import os

reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'],
                     client_secret=os.environ['CLIENT_SECRET'],
                     user_agent='ShowerThoughtsFetcher/1.0')

subreddit = reddit.subreddit('showerthoughts')

posts = list(subreddit.random_rising(limit=10))
random.shuffle(posts)

non_nsfw_posts = [post for post in posts if not post.over_18]

def get_post():
  number = random.randrange(0, len(non_nsfw_posts))

  post_num = 0
  for post in non_nsfw_posts:
    post_num += 1
    if post_num == number:
      return post.title
