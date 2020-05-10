import pandas as pd 

data = pd.read_csv("Twitter_SearchAPI_cleaned.csv") 
data2 = pd.read_csv("newsapicleaned.csv")

edu=0
canada=0
uni=0
dal=0
exp=0
gdsc=0
bdsc=0
fclt=0
cmpsc=0
grad=0

for x in data['Tweet']:
	x = str(x).lower()
	if 'education' in x:
		edu = edu + (x.lower()).count('education')
	if 'canada' in x:
		canada = canada + x.count('canada')
	if 'university' in x:
		uni = uni + x.count('university')
	if 'dalhousie' in x:
		dal = dal + x.count('dalhousie')
	if 'expensive' in x:
		exp = exp + x.count('expensive')
	if ('good school' or 'good schoos') in x:
		gdsc = gdsc + x.count('good school') + x.count('good schools')
	if ('bad school' or 'bad schools' or 'poor school' or 'poor schools') in x:
		bdsc = bdsc + x.count('bad school') + x.count('bad schools') + x.count('poor school') + x.count('poor schools')
	if 'faculty' in x:
		fclt = fclt + x.count('faculty')
	if 'computer science' in x:
		cmpsc = cmpsc + x.count('computer science')
	if 'graduate' in x:
		grad = grad + x.count('graduate')

for x in data2['Content']:
	x = str(x).lower()
	if 'education' in x:
		edu = edu + x.count('education')
	if 'canada' in x:
		canada = canada + x.count('canada')
	if 'university' in x:
		uni = uni + x.count('university')
	if 'dalhousie' in x:
		dal = dal + x.count('dalhousie') 
	if 'expensive' in x:
		exp = exp + x.count('expensive')
	if ('good school' or 'good schoos') in x:
		gdsc = gdsc + x.count('good school') + x.count('good schools')
	if ('bad school' or 'bad schools' or 'poor school' or 'poor schools') in x:
		bdsc = bdsc + x.count('bad school') + x.count('bad schools') + x.count('poor school') + x.count('poor schools')
	if 'faculty' in x:
		fclt = fclt + x.count('faculty')
	if 'computer science' in x:
		cmpsc = cmpsc + x.count('computer science')
	if 'graduate' in x:
		grad = grad + x.count('graduate')


f = open("count.txt","w+")

f.write("Words Frequency \n")

f.write("\n education : %d \n Canada : %d \n University : %d \n Dalhousie : %d \n Expensive : %d \n Good School : %d \n Bad School : %d \n Faculty : %d \n Computer Science : %d \n Graduate : %d " %(edu,canada,uni,dal,exp,gdsc,bdsc,fclt,cmpsc,grad))

f.write("\n\n\n Here all counted words are not case sensitive")
f.close()



