import os;import sqlite3; import win32api #added for the simultaneously warning system
from wordcloud import WordCloud
import matplotlib.pyplot as plt;import re


countSSL=0		#for the pie chart
countNoSSL=0

#connect database, you should close Chrome firstly, otherwise this code will show "database locked" error 
connection = sqlite3.connect('c://Users/safak/AppData/Local/Google/Chrome/User Data/Default/History',timeout=10)

#creatin a cursor
cur=connection.cursor()

#creatin a table, just taking url
cur.execute("SELECT url from urls")

#fetching data from table
results = cur.fetchall()

##ssl checkher algorithm##
subs='https://'
for i in results:
	#print(i)
	filterSSL = len(list(filter(lambda x: subs in x, i)))
	if filterSSL==1:
		countSSL=countSSL+1
	elif filterSSL==0:
		countNoSSL=countNoSSL+1

#if countNoSSL>0:
	#win32api.MessageBox(0,"SSL sertifikası olmayan bir siteye giriş yaptınız" + 'last_visit_time')


res=[''.join(i) for i in results] #tuple list to string
url_addrr = [] #list for the url's
#url_addrr must be a list for the appendding splitted components
#but when you need to visualize it you must transform it to the string again.
for i in range(len(res)):
	temp=res[i].split('/')[2]#second index have addresses
	if "www" in temp:	#if starts with www take first index
		url_addrr.append(temp.split(".")[1])
	else:				#if doesnt start with www take zeroth index
		url_addrr.append(temp.split(".")[0])

#converting list to string

str1=" "#space
url_addrr=str1.join(url_addrr)

#visualizing results#
#print(type(urladdr))# its a string now

labels='Non SSL Certificated Webaddresses', 'SSL Certificated Webaddresses' #label definitons for pie chart
sizes=[countNoSSL, countSSL] #give a value to the chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels,autopct='%1.1f%%', startangle=90),ax1.axis('equal'),plt.show()

wordcloud=WordCloud(collocations=False,width=300, height=300,margin=0).generate(str(url_addrr))#wordclouding
plt.imshow(wordcloud,interpolation="bilinear"),plt.axis("off"),plt.show()

connection.close()