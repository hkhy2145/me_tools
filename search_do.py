import requests
import re
import ast
import codecs
import urllib3
from urllib.parse import urlparse, parse_qs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_response(query):
    url = f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57.3553j0j1&sourceid=chrome&ie=UTF-8&num=100&hl=en&complete=0&safe=off&filter=0&btnG=Search&start=0'
    print(url)
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

    response = requests.get(url,timeout=10, headers=headers,verify=False,proxies=None)
    print(response.text)
    # Check if the request was successful (status code 200)
    if response.status_code == 200 and 'class="g-recaptcha"' not in response.text:
        print("Request was successful!")
        
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
                    print(decoded_url)
                    if query_parameters != {}:
                        open("res7.txt","+a",encoding="utf-8").write(decoded_url+"\n")
        except Exception as e:print(e)
    else:
        print(f"Request failed with status code {response.status_code}")
    
    # Print the response content
    

query='inurl:".php?UserID=" , intext:"student" , site:edu'
query='inurl:".php?tc=" intext:"student"'
get_response(query)
