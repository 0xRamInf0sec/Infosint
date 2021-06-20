import requests
import json
cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m' 
def fuzz():
    dom=input("Enter Domain >> ")
    url="https://sonar.omnisint.io/subdomains/"+dom
    r=requests.get(url)
    print(cyan+"Enumerating Subdomains ^-^ .....")
    for i in r.json():
        print(green+"[+]"+i)
    print(Y+"Subdomain Enumeration Success")
if __name__=="__main__":
    fuzz()