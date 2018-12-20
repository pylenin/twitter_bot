import tweepy
import argparse

parser = argparse.ArgumentParser(description='Provide your tweet')
parser.add_argument('-t', action="store", dest="t")
parser.add_argument('-rt', action="store", dest = "rt")
parser.add_argument('--tl', action="store_true", default=False)
args = parser.parse_args()

consumer_key = '<consumer_key>'
consumer_secret = '<consumer_secret>'

access_token = '<access_token>'
access_token_secret = '<access_token_secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
if args.tl:
    for tweet in api.home_timeline():
        print(tweet.text)
        print(tweet.id)
        print("\n")
if args.t:
    api.update_status(args.t)
    print("Your tweet successfully posted!")
if args.rt:
    api.retweet(args.rt)
    print("Your retweet successfully done!")

