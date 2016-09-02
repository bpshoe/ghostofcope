import praw

user_agent = ("SteelersBot v0.0")


r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("bbottest")

for submission in subreddit.get_hot(limit = 5):



 dir(submission)
 
['approve',
'approved_by',
'author',
 
'domain',
'downs',
'downvote',
'edit',
'edited',
 
'saved',
 
'score',
'secure_media',
'secure_media_embed',
'selftext',
'selftext_html',
 
'title',
 
'ups',
'upvote',
'url',
'user_reports',
'visited',
'vote']




for submission in subreddit.get_hot(limit = 5):
    print "Title: ", submission.title
    print "Text: ", submission.selftext
    print "Score: ", submission.score
    print "---------------------------------\n"
