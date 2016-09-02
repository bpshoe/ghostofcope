import praw
import pdb
import re
import os
from config_bot import *


# check if file exists if not create it
if not os.path.isfile("config_bot.py"):
	print "You must create a config file with you username and password"
	exit(1)

# create reddit instance
user_agent = ("StillersBot v0.0")

r = praw.Reddit(user_agent=user_agent)
# login
r.login(REDDIT_USERNAME, REDDIT_PASS)


#create an empty file if it does not exist this section should be replaced with dynamo db
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []

# load the file into a list and remove empty lines
else: 
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = filter(None, posts_replied_to)

#get hot 5 from subreddit
subreddit = r.get_subreddit('bbottest')
for submission in subreddit.get_hot(limit=5):

	print submission.title

#if submission.id not in posts_replied_to:

