#import required packages
import tweepy
import time
#set up private keys for access
#NOTE: your private key will be different
auth = tweepy.OAuthHandler('naXcR0JCYwXC0S4J5XDwEDkwl','DSPwGhtjLX0zr1Zw0c0Xz0lvHubAyKfp7PVqKDT0Tu9lB0fxwZ')
auth.set_access_token('2821980117-3uOTwpQ1u2FqOzFtjBRmTChS1rcdXIZnwXCXgTZ','Ao9WkRViF3my2ViOP3ooKtajddW6S9rPZwclC2Qo4m63H')
api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.verify_credentials()
#set number of tweets or set search here for easy accessibility
nrTweets = 500
tagList = ''
#loop through each tweet with the key words and filter for no retweets
for tweet in tweepy.Cursor(api.search_tweets, q = 'Tag 3 Friends NFT -filter:retweets', lang = "en", result_type='recent').items(nrTweets):
    #try and except
    try:
        #like, retweet, and follow
        print('Tweet Successfully Liked')
        tweet.favorite()
        print('Tweet Successfully Retweeted')
        tweet.retweet()
        print('Successfully Followed')
        api.create_friendship(user_id=tweet.user.id)
        #get list of followers to tag in tweet
        for follower in tweepy.Cursor(api.get_followers).items():
            if follower.screen_name == 'Account1':
                #set global variables to access later on
                global tag1
                tag1 = follower.screen_name
                tagList = tagList + ' @' + tag1 #+ ' '
            elif follower.screen_name == 'Account2':
                global tag2
                tag2 = follower.screen_name
                tagList = tagList + ' @' + tag2
            elif follower.screen_name == 'Account3':
                global tag3
                tag3 = follower.screen_name
                tagList = tagList + ' @' + tag3
        #tag 3 friends
        print('Successfully Commented')
        #update comment with the tag list
        #api.update_status(status = tagList + '0x9FD62AcF3E83f210Eb7c47c4C9e9454c77b50BbB', in_reply_to_status_id = tweet.id, auto_populate_reply_metadata=True)
        api.update_status(status = tagList, in_reply_to_status_id = tweet.id, auto_populate_reply_metadata=True)
        #empty the string
        tagList = ''
        #30 second break in between each round to prevent spam
        time.sleep(30)
    except tweepy.errors.TweepyException as e:
        print(e)
    except StopIteration:
        break
