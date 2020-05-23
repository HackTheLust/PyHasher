#!/bin/python3
import hashlib
from termcolor import *
def openwordlist(wordlist):
    global f_word
    
    try:
        f_word = open(wordlist, "r")
    except:
        print(colored("[!!] No such file in the directory or provide the full path of the file\n",'red'))
        quit()
print("\n\33[1;36mHash cracking using wordlist\33[0m")
inp_hash = input("\n[$] Enter the hash : ")
wordlist = input("\n[$] Enter the wordlist : ")
a=len(inp_hash)
print(colored("\nPress CTRL+C to exit\n",'yellow'))
openwordlist(wordlist)
#md5-hash-crack
if(a==32):
    print(colored("[$] Found << md5 hash >>\n",'cyan')) 
    for word in f_word:
        a = word.encode()
        a1 = hashlib.md5(a.strip()).hexdigest()
        if a1 == inp_hash:
            print(colored("[+] Found : "+ word,'green'))
            exit()
        else:
            print(colored("[-]",'red'),"Not found : "+ word)

#sha1-hash-crack
elif(a==40):
    print(colored("[$] Found << sha1 hash >>\n",'cyan')) 
    for word in f_word:
        a = word.encode()
        a1 = hashlib.sha1(a.strip()).hexdigest()
        if a1 == inp_hash:
            print(colored("[+] Found : "+ word,'green'))
            exit()
        else:
            print(colored("[-]",'red'),"Not found : "+ word)

#sha224-hash-crack
elif(a==56):
    print(colored("[$] Found << sha224 hash >>\n",'cyan')) 
    for word in f_word:
        a = word.encode()
        a1 = hashlib.sha224(a.strip()).hexdigest()
        if a1 == inp_hash:
            print(colored("[+] Found : "+ word,'green'))
            exit()
        else:
            print(colored("[-]",'red'),"Not found : "+ word)

#sha256-hash-crack
elif(a==64):
    print(colored("[$] Found << sha256 hash >>\n",'cyan')) 
    for word in f_word:
        a = word.encode()
        a1 = hashlib.sha256(a.strip()).hexdigest()
        if a1 == inp_hash:
            print(colored("[+] Found : "+ word,'green'))
            exit()
        else:
            print(colored("[-]",'red'),"Not found : "+ word)

#sha384-hash-crack
elif(a==96):
    print(colored("[$] Found << sha384 hash >>\n",'cyan')) 
    for word in f_word:
        a = word.encode()
        a1 = hashlib.sha384(a.strip()).hexdigest()
        if a1 == inp_hash:
            print(colored("[+] Found : "+ word,'green'))
            exit()
        else:
            print(colored("[-]",'red'),"Not found : "+ word)

#sha512-hash-crack
elif(a==128):
    print(colored("[$] Found << sha512 hash >>\n",'cyan')) 
    for word in f_word:
        a = word.encode()
        a1 = hashlib.sha512(a.strip()).hexdigest()
        if a1 == inp_hash:
            print(colored("[+] Found : "+ word,'green'))
            exit()
        else:
            print(colored("[-]",'red'),"Not found : "+ word)
else:
    print(colored("Invalid Input",'red'))
    exit()
print(colored("\nWordlist don't contain the password!!\n",'red'))
