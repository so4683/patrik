from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("http://www.koros.or.kr/wp/?page_id=3243")

soup = BeautifulSoup(response,"html.parser")

value = soup.find("a",{"class":"category1-text category1-item8"})

print(value)