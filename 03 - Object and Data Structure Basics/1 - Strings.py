text = "hello\nworld"
print(text)

print()

msg0 = 'ichbinoben'
l = len(msg0)
print(l)
print(msg0[3:])
print(msg0[:3])

print()

msg1 = 'Samuel'
msg2 = msg1 + 'awoski'
print(msg2)
print(msg1*3)
print(msg1.upper())

print()

msg3 = "Oh My God"
print(msg3.split())

print()

print("this is a string {}".format("inserted"))
print("this is a string {i}".format(i="inserted"))
print('The {} {} {}'.format('fox', 'cow', 'sheep'))
print('The {2} {0} {1}'.format('fox', 'cow', 'sheep'))
print('The {s} {f} {c}'.format(f='fox', c='cow', s='sheep'))

print()

result = 100/777
result2 = 100*3
print(f'The result is {result}')
print('The result is', result)
print('The result is {}'.format(result))
print('The result is {r}'.format(r=result))
print('The result is {r:1.2f}'.format(r=result))

print()

name = 'Oben'
age = 24
print(type(age))
print(f'Hello, my name is {name} and I am {age} years old')
