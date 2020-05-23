#!/usr/bin/python3
#import pyfiglet
import hashlib
from termcolor import *
#res=pyfiglet.figlet_format("WORD-2-HASH")
#print(res)
#print("\033[1;31m"+"                                                       @HackTheLust"+"\33[0m")
#print()
print("\33[1;36mHash Creation \33[0m\n")
print('''Supported Hash Algorithm

	[+] 1 --> MD5       [+] 2 --> SHA1
	[+] 3 --> SHA224    [+] 4 --> SHA256
	[+] 5 --> SHA384    [+] 6 --> SHA512

	[+] 0 --> EXIT''')
while(True):
    a=input("\n[*] Enter the your choice(in digits) : ")
    if(a=='1'):
        print(colored("\n[*]~$ MD5 Hash is Selected",'cyan'))
        a1=input("\n[*] Enter the word to MD5 : ")
        b1=hashlib.md5(str(a1).encode("UTF-8")).hexdigest()
        print(colored("\nHash : "+b1,'green'))
    elif(a=='2'):
        print(colored("\n[*]~$ SHA1 Hash is Selected",'cyan'))
        a2=input("\n[*] Enter the word : ")
        b2=hashlib.sha1(a2.encode("UTF-8")).hexdigest()
        print(colored("\nHash : "+b2,'green'))
    elif(a=='3'):
        print(colored("\n[*]~$ SHA224 Hash is Selected",'cyan'))
        a3=input("\n[*] Enter the word : ")
        b3=hashlib.sha224(a3.encode()).hexdigest()
        print(colored("\nHash : "+b3,'green'))
    elif(a=='4'):
        print(colored("\n[*]~$ SHA256 Hash is Selected",'cyan'))
        a4=input("\n[*] Enter the word : ")
        b4=hashlib.sha256(a4.encode()).hexdigest()
        print(colored("\nHash : "+b4,'green'))
    elif(a=='5'):
        print(colored("\n[*]~$ SHA384 Hash is Selected",'cyan'))
        a5=input("\n[*] Enter the word : ")
        b5=hashlib.sha384(a5.encode()).hexdigest()
        print(colored("\nHash : "+b5,'green'))
    elif(a=='6'):
        print(colored("\n[*]~$ SHA512 Hash is Selected",'cyan'))
        a6=input("\n[*] Enter the word : ")
        b6=hashlib.sha512(a6.encode()).hexdigest()
        print(colored("\nHash : "+b6,'green'))
    elif(a=='0'):
        print("\n\33[32mHad a good work with you, Good-bye ('-')\33[0m")
        break
    else:
        print(colored("\n ------- Invalid Option,Try again ------- \n",'red'))
