
import tweepy
auth = tweepy.OAuthHandler('6JUnvO96Q8HDO3oPQ1ovu9a1y',
                           'MoZIYs5HGzGv2lBPByI5pm2UvgnJ7UmXDNN0CcaeTh6f8ZQQTk')
auth.set_access_token('1104351004609441794-P1sl9v874vqxsANvGJGpcZZzfJljdv',
                      'Uq6TQG7zZxVvnkIbJrIc7Vnr6ikrknvR67ycbjBoLVhGP')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)