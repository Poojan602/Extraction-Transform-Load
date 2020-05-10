import tweepy as twp
import pandas as pd

consumer_key = 'TKHNgMpFTq5casFMtsYIVtshB'
consumer_secret = '7WAuSWctuLo7woq74PYrxQeot2bZCoo0PBlB9FmZjPXd3KZqjG'
access_token = '917430486980423680-VQym8iqPozAvV7Q36iJm8tnY3siVtCU'
access_token_secret = 'ZUTfJvaM3881LVw1ize6VL93FHu7iACz4cGL4luDXTKMD'

auth = twp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = twp.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

word = "Canada OR University OR 'Dalhousie University' OR Halifax OR 'Canada Education'"

tweets = twp.Cursor(api.search,q=word,lang="en").items(3200)

twts = []
location = []
createdat = []
username = []
scrname = []

for tweet in tweets:
        twts.append(tweet.text)
        location.append(tweet.user.location)
        createdat.append(tweet.created_at)
        username.append(tweet.user.name)
        scrname.append(tweet.user.screen_name)

df = pd.DataFrame({'Tweet':twts,'Location':location,'Created_Date':createdat,'Username':username,'Screen_Name':scrname})
df.to_csv('tweets_SearchAPI.csv',index=False, encoding='utf-8')












