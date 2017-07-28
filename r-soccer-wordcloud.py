import praw
import pprint
from wordcloud import WordCloud
import pickle

reddit = praw.Reddit(client_id='client-id',
                     client_secret='client-secret',
                     user_agent='testscript by /u/testuser')

subreddit = reddit.subreddit('soccer')

all_text = ''
all_posts = []
for submission in subreddit.top(time_filter='month', limit=1000):
    title = submission.title
    all_text += (title + " ")
    all_posts.append(title)

wordcloud = WordCloud(width=1000, height=500).generate(all_text)
wordcloud.to_file('soccer-top-1000-month.png')

pickle.dump(all_posts, open("soccer-top-1000-month.p", "wb"))