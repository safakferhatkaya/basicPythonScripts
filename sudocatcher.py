import os
import datetime

while 1:
komut=input()
os.system(komut) #redirecting the entered command to the terminal with os.system and running


cwd=os.getcwd()
if komut[0:2]=='cd' and komut[2]==' ':#The cd .. commands were not working, that bug was resolved like this

temp=komut.split()
gidilecek_konum=temp[1]#0.index cd, 1.index location
os.chdir(cwd + '/' + gidilecek_konum)

print(os.getcwd())#This command tells you where you are, that's the only thing missing from the terminal


if komut[0:4]=='sudo':
time=datetime.datetime.now()# In order for the clock to be correct in every different recording, it must be inside the statemet
dosya=open("log.txt","a")#file creation and writing processes
dosya.write("sudo komutu kullanildi, tarihi:  "+str(time)+"\n")
dosya.close()
