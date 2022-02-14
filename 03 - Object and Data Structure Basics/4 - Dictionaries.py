myDic = {'key1':'value1', 'key2':'value2'}
print(myDic)
print(myDic['key1'])
prices_lookup = {'apple':2.99, 'orange':3.99, 'milk':4.99}
print(prices_lookup['milk'])

d = {'k1':123, 'k2':[0, 5, 7], 'k3':{'insideKey':5}}
print(d['k2'])
print(d['k3']['insideKey'])
print(d['k2'][2])

d1 = {'k1':123, 'k2':[0, 1, 2], 'k3':77}
print(d1.values())
print(d1.keys())
print(d1.items())