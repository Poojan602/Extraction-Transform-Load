# Extraction-Transform-Load
tweets and news were extracted from twitter and news API based on some keywords. Extracted data were cleaned and then frequency of certain words were counted. For this whole process, python and pandas were used.

## Extraction
Word list ->  Canada, University, Dalhousie University, Halifax, Canada Education

Tweets from Tweeter Search API were extracted which contains any word from word list
Also News were extracted from News API which contains any words from word list
Extracted data were stored in seperate CSV files which can be found <b>CSV/newsapi.csv</b> and <b>CSV/tweets_SearchAPI.csv</b>
The script for scraping data from both these api can be found in <b>python_script/news_api_extraction.py</b> and <b>python_script/twitter_search_api_extraction.py</b> 

## Transform (Cleaning)
After extraction of data, cleaning of those datas were done. 
Cleaning contains removal of special character, emoticons, URL.
Cleaned data were stored in different files other than orginal scraped data which can be found <b>CSV/newsapicleaned.csv</b> and <b>CSV/Twitter_SearchAPI_cleaned.csv</b>
Cleaning script can be found in <b>python_script/cleaning.py</b>

## Frequency Count
word list 2 -> "education", "Canada", "university", "dalhousie", "expensive", "good school" or "good schools", “bad school” or “bad schools” or “poor school” or “poor schools”, "faculty”, “computer science”, “graduate”

Frequncy count of the words in word list 2 were performed on both cleaned data.
Script to count the frequency of those words can be found in <b>python_script/Frequency count.py</b>
The output of those frequency count can be found in <b>Frequency_count_output/count.txt</b>

## Load
The data were stored in MongoDB

## Extra
Data extraction was also performed on Twitter streaming API and both extracted data and script to extract data can be found in <b>extra</b> folder
