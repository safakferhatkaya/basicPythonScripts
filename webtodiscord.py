import requests;import schedule;import time;import discord
from bs4 import BeautifulSoup

bot = discord.Client()
#getting webpage

url = requests.get("https://www.gtu.edu.tr/kategori/301/3/display.aspx","lxml")

#loading the content
htmlContent = url.content
lastAnn=open("lastann.txt","a")
announcement_list=[]
#parse the html and save as txt first element
result = BeautifulSoup(htmlContent,"html.parser")
for link in result.find_all('a'):
    if link.has_attr("href"):   
        if "/icerik/420" in link.attrs["href"]:#icerik/420 for the announcements
            announcement_list.append(link.attrs["href"])
#lastAnn.write(announcement_list[0])#saved to the txt, after this runs will just compare the value, if its differnt save it.
compareAnn = open("lastann.txt", "r")
#print(compareAnn.read())


##what we can do.... save the first, i mean last url to
##.txt formatted database, and every 6 hours, compare the news

if compareAnn.read()==announcement_list[0]:
    print("There is no new announcements")
elif compareAnn.read()!=announcement_list[0]:
    message.channel.send("There is a new announcement : " + str(announcement_list[0]))
    #now save the new announcement to the txt database, as first element
    lastAnn.trunate(0)#clear the txt
    lastAnn.write(compareAnn())#write the new last announcement link


@bot.event

async def on_message(message):
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".  
    if message.content == ("$son gtü duyurusu"):
        await message.channel.send("Last announcement is : " + str(announcement_list[0]))

bot.run("BOTTOKEN")