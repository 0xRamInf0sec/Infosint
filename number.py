import requests
cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'
def number():
    phonenum = input("Enter Mobile Number with country code >> ")
    url = ("http://apilayer.net/api/validate?access_key=cd3af5f7d1897dc1707c47d05c3759fd&number="+phonenum)
    resp = requests.get(url)
    details = resp.json()
    print('')
    print(cyan+"Country : "+ details['country_name'])
    print(cyan+"Location : "+ details['location'])
    print(cyan+"Carrier : "+ details['carrier'])
    
if __name__=="__main__":
    number()
