from bs4 import BeautifulSoup
import urllib.request
import requests
import validators
import time
import config

html_page = urllib.request.urlopen(config.url)
soup = BeautifulSoup(html_page, "html.parser")
ls = set()
broken = false
for link in soup.findAll('a'):
    if(validators.url(link.get("href"))):
        ls.add(link.get("href"))
headers = {
        'Retry-After': '5'
        }
for valid in ls:
      time.sleep(2)
      response=requests.get(valid,allow_redirects=True,headers=headers).status_code
      if(requests.get(valid,allow_redirects=True,headers=headers).status_code!=200):
          print(" Website '{}' is not available or has status code of  {}".format(valid,requests.get(valid,allow_redirects=True,headers=headers).status_code))
          broken = true
     
if not broken:
    print("All links are still intact")
