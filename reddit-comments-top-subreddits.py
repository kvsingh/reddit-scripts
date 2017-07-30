import praw, csv
import time
reddit = praw.Reddit(client_id='your-client-id',
                     client_secret='your-client-secret',
                     user_agent='useragent by /u/testuser')

f = open('reddit-top-1000-post-comments-distr.csv', 'wb')
writer = csv.writer(f)
writer.writerow(['comment_points', 'subreddit', 'id', 'score', 'num_comments'])

subreddit = reddit.subreddit('all')

for submission in subreddit.top(time_filter='year', limit=1000):
    submission.comments.replace_more(limit=0)
    comment_points = []
    for comment in submission.comments.list():
        comment_points.append(comment.score)
    subreddit = submission.subreddit_name_prefixed
    id = submission.id
    score = submission.score
    num_comments = submission.num_comments
    this_submission = [comment_points, subreddit, id, score, num_comments]
    writer.writerow(this_submission)
 
f.close()
