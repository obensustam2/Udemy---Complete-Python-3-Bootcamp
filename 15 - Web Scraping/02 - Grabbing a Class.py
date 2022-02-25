import requests
import bs4

res =requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup)

print()

classes = soup.select('.toctext')
print(classes)
my_class = classes[0].getText()
print(my_class)
