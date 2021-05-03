import requests
from bs4 import BeautifulSoup

link = "https://browser-info.ru/"
responce = requests.get(link).text
soup = BeautifulSoup(responce, "lxml")
block = soup.find("div", id = "tool_padding")

print(block)