import os
import socket
import requests
import sys

def getter():
    login=os.getlogin()
    host=socket.gethostname()
    return login,host

def requester(stickName):
    par={}
    url='http://127.0.0.1:8080/index.html'
    params=getter()
    par['login']=params[0]
    par['host']=params[1]
    par['stickName']=stickName
    try:
        r = requests.get(url,params=par,timeout=5)
        return r.text
    except requests.exceptions.Timeout:
        sys.exit(1)
    except requests.exceptions.TooManyRedirects:
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)
    sys.exit(0)

print requester('blah')
