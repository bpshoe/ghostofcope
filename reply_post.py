import praw
import pdb
import re
import os
from config_bot import *

cope = re.compile('cope', re.IGNORECASE)
myron = re.compile('myron', re.IGNORECASE)
yoistring = re.compile('yoi', re.IGNORECASE)

# check if file exists if not create it
#thisi a test edit foo mo fu
if not os.path.isfile("config_bot.py"):
	print "You must create a config file with you username and password"
	exit(1)

# create reddit instance
user_agent = ("Cope's Ghost v0.0")

r = praw.Reddit(user_agent=user_agent)
# login
r.login(REDDIT_USERNAME, REDDIT_PASS)


#create an empty file if it does not exist this section should be replaced with dynamo db
if not os.path.isfile("comments_replied_to.txt"):
	comments_replied_to = []

# load the file into a list and remove empty lines
else: 
	with open("comments_replied_to.txt", "r") as f:
		comments_replied_to = f.read()
		comments_replied_to = comments_replied_to.split("\n")
		comments_replied_to = filter(None, comments_replied_to)

#set subreddit
subreddit = r.get_subreddit('bbottest')

#get hot 5 posts
for submission in subreddit.get_hot(limit=25):

	print submission.title

	#flattent post comments
	flat_comments = praw.helpers.flatten_tree(submission.comments)

	for comment in flat_comments:

		def yoi():
		    #add a reply
			comment.reply('Yoi!')
			print "Bot replying to: ", comment.body

		def doubleyoi():
		    #add a reply
			comment.reply('Double Yoi!')
			print "Bot replying to: ", comment.body

		actions = ((cope, yoi), (myron, yoi), (yoistring, doubleyoi))

		for word, action in actions:
		    m = re.match(word, comment.body)

		    
		    if m and comment.id not in comments_replied_to: 
		    	print 'success'

		        action()

		        comments_replied_to.append(comment.id)

			with open("comments_replied_to.txt", "w") as f:
			    for comment_id in comments_replied_to:
			        f.write(comment_id + "\n")
			
		        break
	        else:
	        	print 'failed'


	

