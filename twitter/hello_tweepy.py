import tweepy

# consumer
consumer_key = '1edbJ0RswuNVVfmhiXDz3tMtY'
consumer_secret = 'MQleCAeXtNkCHU0P5LHFETPpySxK46bh4A25CxNT76aG6Uq2Hc'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# access
access_token = '17479200-o7Q1EEIXnsQnKlaPJuMlUbBThfLyUVp0sINi6668y'
access_token_secret = 'zkrsRSJNRJwobouNTDRyre0dTrLvFJ4isWOyTepq0T2Rc'
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)