from praw import Reddit

old = Reddit(username='', password='', client_id='', client_secret='',
             user_agent='Transferring NSFW subs from old account to new account (old account)')

new = Reddit(username='', password='', client_id='', client_secret='',
             user_agent='Transferring NSFW subs from old account to new account (new account)')

[new.subreddit(sub.display_name).subscribe() for sub in old.user.me().subreddits() if sub.over18]
