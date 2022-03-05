import requests
import bs4

result = requests.get('http://example.com/')
# print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup)

title = soup.select('h1')
print(title)
print(type(title))

print('')

exact_title = title[0].getText()
print(exact_title)
print(type(exact_title))

print()

paragraph = soup.select('p')
print(paragraph[0])
print(type(paragraph[0]))