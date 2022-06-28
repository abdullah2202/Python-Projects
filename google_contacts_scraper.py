import re
import urllib.request
from bs4 import BeautifulSoup
import sys

urls = []

baseUrl = "https://www.google.com/search?q="

searchUrl = baseUrl + "voip+telephones"
searchPage = urllib.request.Request(searchUrl)
searchPage.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
searchResponse = urllib.request.urlopen(searchPage).read()

searchHTML = searchResponse.decode("utf-8")

searchSoup = BeautifulSoup(searchHTML, "html.parser")
searchDivs = searchSoup.select("#search div.g")

for div in searchDivs:
    alink = div.select('a')
    if(len(alink) >= 1):
        link = alink[0]
        urls.append(link['href'])

