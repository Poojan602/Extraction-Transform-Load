import pandas as pd
import re
import csv 

data = pd.read_csv("~/Desktop/assignment_2/newsapi.csv")

for index,x in enumerate(data.Content):
	data.Content[index] = (re.sub(r"[^a-zA-Z0-9]+",' ',str(x))).strip()   #to remove special characters
	#data.Content[index] = re.sub(r'^https?:\/\/.*[\r\n]*','',y,flags=re.MULTILINE)  #to remove url
	#data.Content[index] = re.sub('<[^<]+?>','',y) #to remove tags

for index,x in enumerate(data.Title):
	data.Title[index] = (re.sub(r"[^a-zA-Z0-9]+",' ',str(x))).strip() #to remove special characters

for index,x in enumerate(data.Author):
	if (pd.isna(x)):
		data.Author[index] = " "
	else:
		data.Author[index] = re.sub(r'^https?:\/\/.*[\r\n]*',' ',str(x),flags=re.MULTILINE)  #to remove url

data.to_csv("~/Desktop/assignment_2/newsapicleaned.csv",index=False,encoding="utf8")


# Twitter SearchAPI data cleaning

data2 = pd.read_csv("~/Desktop/assignment_2/tweets_SearchAPI.csv")

for index,x in enumerate(data2.Tweet):
	#y = re.sub(r'^https?:\/\/.*[\r\n]*','',str(x),flags=re.MULTILINE)  #to remove url
	y = re.sub(r'http\S+','',str(x))  #to remove url
	data2.Tweet[index] = (re.sub(r"[^a-zA-Z0-9]+",'',str(y))).strip()   #to remove special characters

for index,x in enumerate(data2.Location):
	if (pd.isna(x)):
		data2.Location[index] = " "
	else:
		data2.Location[index] = (re.sub(r"[^a-zA-Z0-9]+",' ',str(x))).strip()   #to remove special characters

for index,x in enumerate(data2.Username):
	data2.Username[index] = (re.sub(r"[^a-zA-Z0-9]+",' ',str(x))).strip()   #to remove special characters

data2.to_csv("~/Desktop/assignment_2/Twitter_SearchAPI_cleaned.csv",index=False,encoding="utf8")







