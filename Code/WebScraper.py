from bs4 import BeautifulSoup
import requests

url = "https://www.thekennelclub.org.uk/search/breeds-a-to-z/"
urlrequest = requests.get(url, proxies={"https":"http://10.10.1.9:8888"})
soup = BeautifulSoup(urlrequest.content, 'html5lib')

print (soup)