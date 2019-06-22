import requests
import urllib
import os
import smtplib
import random
import socket
import re
os.system('cls')
print(''' 
$$\   $$\            $$$$$$\                                 
$$ |  $$ |          $$$ __$$\                                
\$$\ $$  | $$$$$$\  $$$$\ $$ |$$\    $$\  $$$$$$\   $$$$$$\  
 \$$$$  / $$  __$$\ $$\$$\$$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
 $$  $$<  $$ /  $$ |$$ \$$$$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
$$  /\$$\ $$ |  $$ |$$ |\$$$ |  \$$$  /  $$   ____|$$ |      
$$ /  $$ |$$$$$$$  |\$$$$$$  /   \$  /   \$$$$$$$\ $$ |      
\__|  \__|$$  ____/  \______/     \_/     \_______|\__|      
          $$ |                                               
          $$ |                                               
          \__|                                                   

Coded by :MOhamad /SO 
                           ''')
print("\n[*] Welcome Xp0ver")
print("\n")
print("ID [1] Admin Login Finder ")
print("ID [2] PhpMyAdmin Finder ")
print("ID [3] Port Scanner ")
print("ID [4] Md5 Crack")
print("\n") 
Id = input("Enter Your Id :  ")
Id = int(Id)

def Finder():
    print("\n\n")
    print("*"*20)
    print("\n")
    print('ADMIN finder')
    print("\n")
    print("*"*20)
    print("\n")
    print("\n")
    l = 2 
    if l == 2:
        site = input(">>> Enter Your Site  :    ")
        if 'http://' in site:
            site = site
        else:
            site = 'http://' + site
        print("\n\n")
        print("<?>  Check Url ...")
        print("\n")
        u = requests.get(site)
        if u.status_code == 200 :
            print("<+>  Website ON  :   ",site)
        else:
            print("<->  Website Down  :   ",site)
            exit
        print("\n\n")
        patch = open('list.txt')
        for admin in patch:
            try:
                s = site + '/' + admin
                s = str(s)
                url = urllib.request.urlopen(s)
                print("<+!>  Finded Admin  :   ",s)
                break
            except urllib.error.URLError:
                print("<-?>  No Admin  :   ",s)
                continue
                print("\n")
                input("Enter your continue")
def phpmyadmin():
    os.system('cls')
    site = input(">>> Enter Your Target Site  :  ")
    if 'http://' or 'https://' in site:
        site = site
    else:
        site = "http://" + site
    print("\n")
    print("Pless Wait Online Website ...")
    try:
        s = urllib.request.urlopen(site)
        if s.code == 200:
            print("[+] Website Online")
            print("\n")
    except urllib.error.URLError:
        print("Website Oflinne ...")
        quit
    wordlist = open('phpmyadmin.txt')
    for i in wordlist:
        u = site + i
        u = str(u)
        try:
            url = urllib.request.urlopen(u)

            if url.code == 200:
                print("[+] Finded Php My admin Login  :   ",str(u),"\n")
                quit
        except urllib.error.URLError:
            print("[-] Wrinng PhpMyAdmin  :   ",u,"\n")            
def Port_Scanner():
    print("\n")
    p = []
    port = [21,22,23,24,18,445,70,25,50,55,80,443,4444,13,12]
    ip = input("\n[!] Pless Wait Enter Ip  :    ")
    l = []
    print("\nPless Wait Scaniing ...")
    for p in port:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        test = sock.connect_ex((ip,p))
        if test == 0:
            print("\n[Open]  Ip  :  " + ip + "  Port  : ",str(p))
            l.append(p)
        else:
            print("\n[Not Open] Ip  :   " + ip + "  Port  :   ",str(p))
    print("\n\n List Port Open  :   ",l)

def Md5_Crack():
    os.system('cls')
    print('''
                    $$\ $$$$$$$\                                               $$\                           
                    $$ |$$  ____|                                              $$ |                          
$$$$$$\$$$$\   $$$$$$$ |$$ |             $$$$$$$\  $$$$$$\  $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$  _$$  _$$\ $$  __$$ |$$$$$$$\        $$  _____|$$  __$$\ \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
$$ / $$ / $$ |$$ /  $$ |\_____$$\       $$ /      $$ |  \__|$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
$$ | $$ | $$ |$$ |  $$ |$$\   $$ |      $$ |      $$ |     $$  __$$ |$$ |      $$  _$$<  $$   ____|$$ |      
$$ | $$ | $$ |\$$$$$$$ |\$$$$$$  |      \$$$$$$$\ $$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
\__| \__| \__| \_______| \______/        \_______|\__|      \_______| \_______|\__|  \__| \_______|\__|      
                                                                                                                                                                                                                                                                                                                          
	\n\n''')
    Hash = input("\n\n[+] Enter Your Hash (Md5)  :   ")
    if(len(Hash) <= 31):
        os.system('cls')
        print("[-] Is Hash Bad Format")
        print("Pless Exit Aplicetion ...")
    global hash
    def SiteMd5Online():
        url = 'https://www.md5online.org/md5-decrypt.html'
        url = str(url)
        datat = {'hash' : Hash}
        Send_Web = requests.post(url,data=datat)
        if('Found' in Send_Web.text):
            Dycrypt = re.search(r'<b>(.*?)</b>',Send_Web.text).group(1)
            print("\n\n[+] Found Is Hash Database MD5online.com  :    ",Dycrypt)
        else:
            print("\n\n[-] Not Found Hash Database Md5online.com")
    def md5_gromweb():
        url = "https://md5.gromweb.com/?md5="+ Hash
        url = str(url)
        Grom_web = requests.get(url)
        if('was succesfully' in Grom_web.text):
            Decrypt = re.search(r'<em class="long-content string">(.*?)</em>',Grom_web.text).group(1)
            print("\n\n[+] Found Is Hash Database MD5gromweb.com  :    ",Decrypt)
        else:
            print("\n\n[-] Not Found Hash Database MD5gromweb.com ")
    def hashtoolkit():
        url = 'http://hashtoolkit.com/reverse-hash/?hash='+Hash
        toolkit = requests.get(url)
        if('Decrypt Hash' in toolkit.text):
            Decrypt = re.search(r'<span title="decrypted md5 hash">(.*?)</span>', toolkit.text).group(1)
            print("\n\n[+] Found Is Hash Database hashtoolkit.com :    ",Decrypt)
        else:
            print("\n\n[-] Not Found Hash Database hashtoolkit.com ")
    SiteMd5Online()
    md5_gromweb()
    hashtoolkit()
if Id == 1 :
    Finder()
if Id == 2:
    phpmyadmin()
if Id == 3:
    Port_Scanner()
if Id == 4:
    Md5_Crack()