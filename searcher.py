import time
from tqdm import tqdm
import requests
import re
import ast
import codecs
from urllib.parse import urlparse, parse_qs
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
good_count = 0
bad_count = 0
#data=['inurl:"?user_id=" site:.edu','inurl:"?user_id=" site:.is']#
data=open("dork_u.txt" ,"+r",encoding="utf-8").readlines()
total_iterations = len(data)
#########################################################
import os
import random
import time
from subprocess import Popen , PIPE
import requests
import os
ns=os.listdir(os.getcwd()+"\\configs")
def di2():
    k='"c:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --command disconnect_all'#ns[sen]
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
def co(x):
    global sen,sk,sni
    #os.chdir(os.getcwd()[0]+':\\Program Files\\OpenVPN\\bin\\')
    k='"c:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --command connect '+x
    #print(k)
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
def ch_st(sn):
    sn1=sn.replace(".ovpn", ".log")
    l=open("log\\"+sn1,"r").readlines()
    for i in l:
        if "Initialization Sequence Completed" in i:
            return True
        elif "RESOLVE: Cannot resolve host address:" in i or "RECONNECTING" in i:
            return -1
    return 0
def ch_go(sn):
    r=requests.get("http://www.google.com")
    #print(r.status_code)
    if r.status_code != 200 or 'class="g-recaptcha"' in r.text :
        open("badserver\\g\\bad.txt","+a").write(sn+"\n")
        #print("bad")
        return False
    open("badserver\\g\\god.txt","+a").write(sn+"\n")
    return True
def change_ip():
    connect=False
    while not connect:
        sn=ns[random.randint(0,len(ns)-1)]#"ipvanish-MX-Guadalajara-gdl-c07.ovpn"#
        di2()
        co(sn)
        tryn=0
        for i in range(5):
            time.sleep(5)
            tryn+=1
            try:
                red=(ch_st(sn))
                #print(red)
                if True==red:
                    connect=ch_go(sn)
                    break
                elif -1==red:
                    connect=False
                    break
                elif 0==red and tryn>=4 :
                    open("badserver\\c\\bad.txt","+a").write(sn+"\n")
                else:
                    pass
            except Exception as e:
                pass
                #print(e)
    return True
    




#########################################################
"""**************************************************"""
def log_data(x):
    open("log_data.txt","+a",encoding="utf-8").write(str(time.gmtime())+"\n"+"\n"+str(x)+"\n"+"\n")
"""**************************************************"""
def search(query,proxy=None):
    global b,good_count
    url = f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57.3553j0j1&sourceid=chrome&ie=UTF-8&num=200&hl=en&complete=0&safe=off&filter=0&btnG=Search&start=0'
    headers = {
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Sec-GPC": "1",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
    }
    try:
        response = requests.get(url,timeout=10, headers=headers,verify=False,proxies=proxy)
        
    except Exception as e:
        response='bad'
        log_data('get response'+str(e))
    # Check if the request was successful (status code 200)
    if 'bad' != response and response.status_code == 200 and 'class="g-recaptcha"' not in response.text:
        #print("Request was successful!")
        try:
            s=re.findall(r'jsdata="MuIEvd;_;(.*?)">',response.text)[0]
            pattern = s+"(.*?);var a=m"

            # Use re.findall to extract the value
            matches = re.findall(pattern,response.text)
            k=str(matches[0]).split('x22')
            m=str("['1"+matches[0])
            k_list=ast.literal_eval(m)
            for i in k_list:
                if i[:len('["http')] == '["http':
                    p_list=re.findall(r'"(.*?),',i)
                    u=p_list[0][:-1]
                    decoded_url = codecs.decode(u, 'unicode_escape')
                    parsed_url = urlparse(decoded_url)
                    query_parameters = parse_qs(parsed_url.query)
                    if query_parameters != {}:
                        open("urlsql.txt","+a",encoding="utf-8").write(decoded_url+"\n")
                    good_count+=1
        except Exception as e:log_data('scrap --->'+str(e))
        return True
    else:
        try:
            change_ip()#r_openvpn=requests.get("http://127.0.0.1:100/api/message?key=secret_key&msg=s")
            #print(r_openvpn)
        except Exception as e:
            log_data('change ip'+str(e))
        #print(f"Request failed with status code {response.status_code}")
        return False
    # Print the response content

"""**************************************************"""

# Create a tqdm progress bar
"""**************************************************"""
with tqdm(total=total_iterations, ascii=True, ncols=100) as pbar:
    for i in data:
        # Simulate a task that takes some time
        time.sleep(0.1)
        # Simulate a condition where something can be either "good" or "bad"
        while not search(i[:-1]):
            time.sleep(5)
            bad_count += 1
        
        # Update the progress bar
        pbar.update(1)
        
        # Update the displayed message
        pbar.set_description(f"Good: {good_count} Bad: {bad_count}")

# Display the final result
print(f"Result: Good: {good_count} Bad: {bad_count}")

