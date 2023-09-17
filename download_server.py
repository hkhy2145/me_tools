import requests
import re
r=requests.get("https://configs.ipvanish.com/configs/")
t=re.findall(r'<a href="ipvanish-(.*?)">',r.text)
print(t)
print(len(t))
for i in t:
    r=requests.get(f"https://configs.ipvanish.com/configs/ipvanish-{i}")
    open("C:\\Users\\Administrator\\Desktop\\ip\\"+str(i),"+a",encoding="utf-8").write((r.text.replace("keysize 256\n", "")).text.replace("auth-user-pass", "auth-user-pass pass"))
r=requests.get(f"https://configs.ipvanish.com/configs/ca.ipvanish.com.crt")
open("C:\\Users\\Administrator\\Desktop\\ip\\"+"ca.ipvanish.com.crt","+a",encoding="utf-8").write(r.text)
pass1="davecurtislongoria@yahoo.com"+"\n"+"Dave8600"
open("C:\\Users\\houss\\Desktop\\python\\"+"pass","+a",encoding="utf-8").write(pass1)
print("endd")

