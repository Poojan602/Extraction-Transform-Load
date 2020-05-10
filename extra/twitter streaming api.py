import tweepy as twp
import pandas as pd

consumer_key = 'TKHNgMpFTq5casFMtsYIVtshB'
consumer_secret = '7WAuSWctuLo7woq74PYrxQeot2bZCoo0PBlB9FmZjPXd3KZqjG'
access_token = '917430486980423680-VQym8iqPozAvV7Q36iJm8tnY3siVtCU'
access_token_secret = 'ZUTfJvaM3881LVw1ize6VL93FHu7iACz4cGL4luDXTKMD'

auth = twp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = twp.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

twts = []
location = []
createdat = []
username = []
scrname = []

class StreamListener(twp.StreamListener):
	counter = 0
	def on_status(self,status):
		if(self.counter < 3200):
			self.counter += 1
			twts.append(status.text.encode("UTF-8"))
			location.append(status.user.location)
			createdat.append(status.created_at)
			username.append(status.user.name)
			scrname.append(status.user.screen_name)
			return True
		else:
			return False

stream_listener = StreamListener()
stream = twp.Stream(auth=api.auth, listener=stream_listener,lang="en")
stream.filter(track=["Canada", "University", "Dalhousie University", "Canada Education", "Halifax"])

df = pd.DataFrame({'Tweet':twts,'Location':location,'Created_Date':createdat,'Username':username,'Screen_Name':scrname})
df.to_csv('tweets_StreamAPI.csv',index=False, encoding='utf-8')


