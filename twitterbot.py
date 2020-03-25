import tweepy   
import time  
 

auth = tweepy.OAuthHandler("your_codes")
auth.set_access_token("your_secret_keys")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
c=0
user = api.me()

search_list = [your_search_queries]

for search in search_list: 
    for tweet in tweepy.Cursor(api.search, search).items(100):
        try:
            tweet.favorite()
            print("tweet liked")
            time.sleep(10)
            c+=1
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(10)
        except StopIteration:
            break
    print(f'{search} is done, liked {c} tweets')