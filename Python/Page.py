import requests as r
from bs4 import BeautifulSoup as B
url = "https://www.pracuj.pl/praca/python;kw?rd=0"
page = r.get(url)
soup= B(page.content, "html.parser")
print(soup.title.text) 
print(soup.find('span',class_="results-header__offer-count-text-number").text)
