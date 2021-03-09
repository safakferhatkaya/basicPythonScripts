import os
import datetime

while 1:
komut=input()
os.system(komut) #girilen komutu sisteme yonlendirip calistirma


cwd=os.getcwd()
if komut[0:2]=='cd' and komut[2]==' ':#cd .. komutları çalışmıyordu, o bug boyle cozuldu

temp=komut.split()
gidilecek_konum=temp[1]#0. index cd, 1. index konum
os.chdir(cwd + '/' + gidilecek_konum)

print(os.getcwd())#bu komut, size nerede oldugunuzu soyler, terminalden tek eksigi bu idi


if komut[0:4]=='sudo':
time=datetime.datetime.now()#her farkli kayitta saatin dogru olmasi icin if statemetin icinde olmali
dosya=open("log.txt","a")#dosya olusturma ve yazma islemleri
dosya.write("sudo komutu kullanildi, tarihi:  "+str(time)+"\n")
dosya.close()