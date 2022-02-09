
mylist = ["one", "two", "three"]
mylist2 = [1, 2, 3]
print(mylist[2])
print(mylist2[2])
print(mylist+mylist2)
mylist2[0] = 4
print(mylist2)
mylist.append("four") # yeni bir eleman listeye ekleniyor
print(mylist)
mylist.pop() # istenilen eleman listeden siliniyor
print(mylist)
mylist.pop(1)
print(mylist)

new_list = ['a', 'x', 'e', 'b', 'c']
num_list = [1, 4, 7, 3, 0]
new_list.sort() # listeyi alfabetik veya sayısal olarak baştan sona sıralıyor
print(new_list)
num_list.sort()
print(num_list)
new_list.reverse() # listeyi alfabetik veya sayısal olarak sondan başa sıralıyor
print(new_list)

List= [1, 2, [3, 4], [5, 6, 7]]
print(List[2][1])
print(List[3][2])