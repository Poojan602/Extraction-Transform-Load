from newsapi import NewsApiClient
import pandas as pd

newsapi = NewsApiClient(api_key='ed86d70b1c20452e8abfb3e5046c8b93')

word = "Canada OR University OR 'Dalhousie University' OR Halifax OR 'Canada Education'"

title = []
author = []
pubdt = []
cnt = []
desc = []

for index,loop in enumerate(range(5)):
        all_articles = newsapi.get_everything(q=word,language='en',page=index+1)
        for news in all_articles['articles']:
        	title.append(news['title'])
        	desc.append(news['description'])
        	author.append(news['author'])
        	pubdt.append(news['publishedAt'])
        	cnt.append(news['content'])

df = pd.DataFrame({'Title':title,'Author':author,'Description':desc,'Published_At':pubdt,'Content':cnt})
df.to_csv('newsapi.csv',index=False, encoding='utf-8')
