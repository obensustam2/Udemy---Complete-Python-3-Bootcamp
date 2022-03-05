# GOAL: Get title of every book with a 2 star rating

import requests
import bs4

book_store = 'https://books.toscrape.com/catalogue/page-{}.html'
res = requests.get(book_store.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)

product_pod = soup.select('.product_pod')
# print(product_pod)
# print(type(product_pod))
# print(len(product_pod))

first_book = product_pod[0]
# print(first_book)
three_star = first_book.select('.star-rating.Two')
# print(three_star)
book_name = first_book.select('a')[1]['title']
book_name = first_book.select('a')
# print(book_name)

####LOOP####
book_store = 'https://books.toscrape.com/catalogue/page-{}.html'
two_star_book_list = []

for i in range(1,51):
    res = requests.get(book_store.format(i))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    product_pod = soup.select('.product_pod')
    print(i)
    for i in range(19):
        book = product_pod[i]
        three_star = book.select('.star-rating.Two') # put . instead of space

        if len(three_star):
            two_star_book_list.append(book.select('a')[1]['title'])

for book in two_star_book_list:
    print(book)

    