# Add module to play around twitter api
import tweepy

# authorise the twitter consumer api key and secret key
auth = tweepy.OAuthHandler('6JUnvO96Q8HDO3oPQ1ovu9a1y',
                           'MoZIYs5HGzGv2lBPByI5pm2UvgnJ7UmXDNN0CcaeTh6f8ZQQTk')

# set access token and secret token
auth.set_access_token('1104351004609441794-P1sl9v874vqxsANvGJGpcZZzfJljdv',
                      'Uq6TQG7zZxVvnkIbJrIc7Vnr6ikrknvR67ycbjBoLVhGP')

# authorise to apis
api = tweepy.API(auth)

# fetch home timeline and store in public_tweets variable
public_tweets = api.home_timeline()

# Loop through public_tweets
for tweet in public_tweets:
    # print text of the tweets
    print(tweet.text)