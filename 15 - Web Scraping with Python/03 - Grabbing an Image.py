import requests
import bs4

# Get Image Link from Website
res =requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, 'lxml')
img = soup.select('.image')
first_img = img[0]
print(first_img)
# first_img_src = first_img['src']
# print(first_img_src)

# Save Image at Specific Url
img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg'
img_res = requests.get(img_url)
img_content = img_res.content
# print(img_content)
f = open('my_computer_image.jpg','wb') #write binary mode
f.write(img_content)
f.close()