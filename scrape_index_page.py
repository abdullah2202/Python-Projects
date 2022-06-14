# Scrapes an 'index of' page of a website and downloads all files to a local folder
#
# Used: https://stackoverflow.com/a/61140905 to handle file downloads requiring a login
# Used: https://curl.trillworks.com/ to convert cURL to python requests

import re
import requests
from bs4 import BeautifulSoup

url = "https://www.domain.com/folder/to/files/"

cookies = {
    'PHPSESSID': '268e5176e3815983c272a808f7d0760e',
}

headers = {
    'authority': 'www.domain.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US;q=0.5',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=268e5176e3815983c272a808f7d0760e',
    'referer': 'https://www.domain.com/folder/to/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
}

# Request.get index page with cookies and headers to allow when login is needed
page = requests.get(url, cookies=cookies, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

# Get all <a href/> tags
alinks = soup.find_all('a')

for link in alinks:
    if link.has_attr('href'):
        href = link['href']
        if((href[-1] != "/") and (href[0] != "?")): # Ignore directories and navigation links
            urllink = url+href
            folder = 'G:\Local\Folder\Downloaded\\'
            path = folder+href
            r = requests.get(urllink, stream=True, cookies=cookies, headers=headers)
            print("Downloading: "+path)
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
                print("Saved: "+href)
