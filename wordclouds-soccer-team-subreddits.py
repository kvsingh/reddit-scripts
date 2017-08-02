import praw
from wordcloud import WordCloud
import pickle

reddit = praw.Reddit(client_id='your-client-id',
                     client_secret='your-client-secret',
                     user_agent='app-name by /u/testuser')

for subreddit_name in ['chelseafc', 'soccer', 'Gunners', 'reddevils', 'coys', 'MCFC', 'borussiadortmund', \
                       'Barca', 'realmadrid', 'fcbayern']:
    subreddit = reddit.subreddit(subreddit_name)
    all_text = ''
    for submission in subreddit.top(time_filter='month', limit=1000):
        title = submission.title
        all_text += (title + " ")

    wordcloud = WordCloud(width=1000, height=500).generate(all_text)
    wordcloud.to_file('wordclouds/' + subreddit_name + '-top-1000-month.png')
