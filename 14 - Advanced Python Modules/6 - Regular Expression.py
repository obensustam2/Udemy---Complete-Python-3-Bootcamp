import re

text = "The agent's phone number is 408-55-1234. Call soon!"
print('phone' in text) 

print()

pattern = 'phone'
a = re.search(pattern, text)
print(a)
print(a.span())

print()

pattern2 = 'oben'
b = re.search(pattern2, text)
print(b)

print()

text2 = 'phone phone phone'
c = re.findall(pattern, text2)
e = re.search(pattern, text2)
print(c)
print(e)

print()

text = "My telephone number is 124-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone)
print(phone.group())

print()

d = (re.search(r"man|woman","This man was here."))
print(d)