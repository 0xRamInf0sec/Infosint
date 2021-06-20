import requests
import webbrowser

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'
def iplocate():
    ipinfo={}
    ip=input("Ip address >> ")
    url="http://ip-api.com/json/"+ip
    r=requests.get(url)
    ipinfo=r.json()
    if ipinfo['status'] == 'success':
        lat=ipinfo['lat']
        lon=ipinfo['lon']        
        print(green+"Ip location Found !!")
        print('Country     : ',ipinfo['country'])
        print('Region Name : ',ipinfo['regionName'])
        print('City        : ',ipinfo['city'])
        print('Time zone   : ',ipinfo['timezone'])
        print('ISP         : ',ipinfo['isp'])
        print(cyan+'Opening Location in browser')
        mapurl = "https://maps.google.com/maps?q=%s,+%s" % (lat, lon)
        webbrowser.open(mapurl, new=2) 
        print('')
    else:
        print(red+"Ip location Not Found !!")
        
    
        
if __name__=="__main__":
    iplocate()
