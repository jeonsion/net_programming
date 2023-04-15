A_list = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']
A_list.append("!")
print(A_list)
del A_list[4]
print(A_list)
A_list.insert(4, 'a')
print(A_list)
print(''.join(A_list))

A_list.sort(reverse =True)
print(A_list)