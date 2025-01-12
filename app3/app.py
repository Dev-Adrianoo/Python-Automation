import requests 
from bs4 import BeautifulSoup

LINK = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

requesicao = requests.get(LINK, headers=headers)

print(requesicao)

site = BeautifulSoup(requesicao.text, "html.parser")

Title = site.find("title")
print(Title)

valorDolar = site.find("class", class_="IZ6rdc")
print(valorDolar)