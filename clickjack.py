from urllib.request import urlopen
cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'
def ClickJacking():
    host=input("Enter host >>")
    port=int(input("Enter port >>"))
    if port == 80:
          port = 'http://'
    elif port == 443:
          port = 'https://'
    else:
         print("Could'nt fetch data for the given PORT")


    url = (port+host)

    data = urlopen(url)
    headers = data.info()

    if not "X-Frame-Options" in headers:
          print(green+"Website is vulnerable to ClickJacking")

    else:
        print(red+"Website is not Vulnerable to ClickJacking")
if __name__=="__main__":
    ClickJacking()