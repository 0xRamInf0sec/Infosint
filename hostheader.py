import requests
cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'
def HostHeader():
    host=input("Enter host >> ")
    port=int(input("Enter port >> "))    
    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print(red+"Could'nt fetch data for the given PORT")
    url = (port + host)
    headers = {'Host': 'http://evil.com'}
    response = requests.get(url, headers=headers)
    if 'evil.com' in response.headers:
        print(green+"Vulnerable to Host Header Injection")
    else:
        print(red+"Not Vulnerable to Host header injection")
if __name__=="__main__":
    HostHeader()