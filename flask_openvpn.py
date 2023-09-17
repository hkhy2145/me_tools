from flask import Flask, request
import os
import subprocess
import time
import sys
import random
import requests
from subprocess import Popen , PIPE
from _thread import *
import threading
import psutil
nd=[]
ns=os.listdir(os.getcwd()+"\\x")
def c_open():
    return ('172.' in str(psutil.net_if_addrs()["OpenVPN TAP-Windows6"][1]))
try:
    ns.remove('ca.ipvanish.com.crt')
    ns.remove('editcf.py')
    ns.remove('pass')
except:
    pass
sen=''
def co(x):
    global sen,sk,sni
    os.chdir(os.getcwd()[0]+':\\Program Files\\OpenVPN\\bin\\')
    k='openvpn-gui.exe --command connect '+x
    print(k)
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
def di():
    k='TASKKILL /F /IM openvpn-gui.exe'
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
    k='TASKKILL /F /IM openvpn.exe'
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
    k='TASKKILL /F /IM openvpnserv.exe'
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
    k='TASKKILL /F /IM openvpnserv2.exe'
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
def di2():
    os.chdir('C:\\Program Files\\OpenVPN\\bin\\')
    k='openvpn-gui.exe --command disconnect_all'#ns[sen]
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
def di1():
    t2 = threading.Thread(target = di2)
    t2.start()
app = Flask(__name__)
API_KEY = "secret_key"

@app.route('/api/message', methods=['GET'])
def receive_message():
    global ns
    # Get the API key from the URL parameter
    message = request.args.get('msg')
    if message =="s":
        di2()
        while not c_open():
            s=ns[random.randint(0,len(ns)-1)]
            t1 = threading.Thread(target = co(s))
            t1.start()
            print('delay to connect')
            for i in range(8):
                time.sleep(1)
                if c_open():
                    return 'god'
        return 'bad'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=100, debug=False)


