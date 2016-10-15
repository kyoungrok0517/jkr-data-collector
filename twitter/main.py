import tweepy
import time
from pprint import pprint
from tweepy.error import TweepError


def init_api():
    # consumer
    consumer_key = '1edbJ0RswuNVVfmhiXDz3tMtY'
    consumer_secret = 'MQleCAeXtNkCHU0P5LHFETPpySxK46bh4A25CxNT76aG6Uq2Hc'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # access
    access_token = '17479200-o7Q1EEIXnsQnKlaPJuMlUbBThfLyUVp0sINi6668y'
    access_token_secret = 'zkrsRSJNRJwobouNTDRyre0dTrLvFJ4isWOyTepq0T2Rc'
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

if __name__ == '__main__':
    api = init_api()

    for l in api.lists_all():
        owner_screen_name = l.user.screen_name
        slug = l.slug

        try:
            for item in tweepy.Cursor(api.list_timeline, owner_screen_name=owner_screen_name, slug=slug).items(10):
                print(item.text)
        except TweepError as e:
            print(e)

