#!/bin/python3
import os
import pyfiglet
res=pyfiglet.figlet_format("  PyHasher")
print("\33[1;36m"+res+"\33[0m")
print("\033[1;31m"+"                                     @HackTheLust"+"\33[0m")
print()
print('''PyHasher :-

        |- 1 --> [*] Hash Creation
	 
	|- 2 --> [*] Hash Cracking using wordlist
	 
	|- 0 --> [*] Exit''')

while(True):

    x=input("\n\33[1;32m[$]~# >>> \33[0m")

    if(x=="1"):
        os.system('clear' if os.name=='posix' else 'cls')
        os.system("python3 ./subfiles/createhash.py")
    elif(x=="2"):
        print()
        print(''' Supported Hash Algorithm
		[+] 1 --> MD5       [+] 2 --> SHA1
		[+] 3 --> SHA224    [+] 4 --> SHA256
		[+] 5 --> SHA384    [+] 6 --> SHA512''')
        y=input("\nDo you want full verbose details(Y/n) : ")
        if(y=="y" or y==""):
            os.system('clear' if os.name=='posix' else 'cls')
            os.system("python3 ./subfiles/crack.py")
        else:
            os.system('clear' if os.name=='posix' else 'cls')
            os.system("python3 ./subfiles/crack2.py")
    elif(x=="0"):
        print("\n\33[32mHad a good time with you, bye!!\33[0m\n")
        break
    else:
        print("\n\33[31m----- Invalid Input -----\33[0m\n")
