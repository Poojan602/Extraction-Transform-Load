import re
import csv 
import pandas as pd 


inputfile = csv.reader(open('Twitter_SearchAPI_cleaned.csv', 'r'))

for row in inputfile:
	print(row[0])
	print('\n')
