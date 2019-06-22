names = ['john', 'bob', 'sarah', 'mary']

print(names)
print(names[0])
print(names[2])
print(names[1:3])

names[0] = 'jon'
print(names)


matrix = [
    [1,2,3],
    [5,6,7],
    [8,9,0]
]
print(matrix[0][1])

for row in matrix:
    for col in row:
        print()# print(col)

list = [1,2,3,4,5,6]

list.append(7)

list.insert(1,1.5)

list.remove(1.5)

# list.clear()

list.pop()

print(list.index(5))
print(5 in list)

list.append(5)
print(list.count(5))

list.sort()
list.reverse()
print(list)

listt = list.copy()
#listt = list -----points
print(listt)


tuple = (1,2,3) #could not be modified
print(tuple[0])