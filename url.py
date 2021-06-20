
import requests
import time
from datetime import datetime

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'

def urlinfo():
    print(Y+"Note : URL = http://example.com")
    url=input("URL >> ")
    print("-"*50)
    print(cyan+"          Trace Results        ")
    print("-"*50)
    try:
        r = requests.get(url) 
        print()
        current_datetime = datetime.now()
        print("[+]Traced Date and Time :",current_datetime)
        print(green+"[-]"+"301 Redirected")
        print(cyan+"[-]"+r.url)  
    except Exception as e:
        print(red+"Error Occured :"+e)
    
if __name__=="__main__":
    urlinfo()