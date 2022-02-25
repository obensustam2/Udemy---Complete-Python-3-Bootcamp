import requests
import bs4

quote_store = 'https://quotes.toscrape.com'
res = requests.get(quote_store.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)


## Get the names of all the authors on the first page.
auther_all = soup.select('.author')
#print(auther_all)
auther_set = set() # non-repetitive
auther_list = []
for auther in auther_all:
    auther_set.add(auther.text)
    auther_list.append(auther.text)
# print(auther_set)
for a in auther_list:
    # print(a+'\n')
    pass

## Create a list of all the quotes on the first page.
quotes_all = soup.select('.text')
quote_list = []
for quote in quotes_all:
    quote_list.append(quote.text)
for q in quote_list:
    # print(q+'\n')
    pass


## Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from 
## the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote, try 
## to find a class only present in the top right tags, perhaps check the span.
tag_all = soup.select('.tag-item')
tag_list = []
for tag in tag_all:
    tag_list.append(tag.text)
for t in tag_list:
    # print(t+'\n')
    pass

## loop through all the pages and get all the unique authors on the website
## SOLUTION 1
author_set = set()
quote_store = 'https://quotes.toscrape.com/page/{}/'

for i in range(1,11):
    res = requests.get(quote_store.format(i))
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select('.author'):
        auther_set.add(name.text)
# print(auther_set)


## SOLUTION 2
new_page = quote_store.format(999)
res = requests.get(new_page)
soup = bs4.BeautifulSoup(res.text, 'lxml')
state = "No quotes found!" in res.text
print(state)

quote_store = 'https://quotes.toscrape.com/page/{}/'
while state:
    res = requests.get(quote_store.format(i))
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select('.author'):
        author_set.add(name.text)
    i += 1
    if "No quotes found!" in res.text:
        state = False
print(author_set)

# new_page = quote_store.format(2)
# res = requests.get(new_page)
# print(res.text)
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# my_list = soup.select('.author')
# print(type(my_list))
# print(len(my_list))