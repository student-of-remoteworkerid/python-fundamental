book_list = ['Seven Habits', 'How to Influence people', 'First Things First']
print('Display variable book list')
print(book_list)

print('\nProcess all book list with for')
for i in book_list:
    print(i)

print('\nDisplay content from book list from based on specific index')
print(book_list[0])
print(book_list[2])

print('\nDisplay book list with for in range')
for i in range(0, len(book_list)):
    print(book_list[i])

book_list = [1, 'Kenji Volume 2', -313, 3.14]
print('\nDisplay book list with for in range and with difference element type')
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nBack to initial value of book list')
book_list = ['Seven Habits', 'How to Influence people', 'First Things First', '40X']
print('\nadd 1 new book')
book_list.append('Dunia Matematika Kelas 5')

for i in range(0, len(book_list)):
    print(book_list[i])

print('\nClear list')
book_list.clear()
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nChange first element')
book_list = ['Seven Habits', 'How to Influence people', 'First Things First', '40X']
book_list[0] = 'Eight Habits'
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nTake second element')
book = book_list.pop(1)
for i in range(0, len(book_list)):
    print(book_list[i])

print('\npicked up previously book')
print(book)

print('\nPop')
book_list.pop()
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nPop -1')
book_list = ['Seven Habits', 'How to Influence people', 'First Things First', '40X']
book_list.pop(-1)
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nDelete')
book_list = ['Seven Habits', 'How to Influence people', 'First Things First', '40X']
del book_list[0]
for i in range(0, len(book_list)):
    print(book_list[i])

# Slice
print('\nDelete with slice')
book_list = ['Seven Habits', 'How to Influence people', 'First Things First', '40X']
del book_list[0:-2] # start: end
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nDelete with slice start, end and step')
book_list = ['Seven Habits', 'How to Influence people', 'First Things First', '40X']
del book_list[0::2] # start:end:step
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nCreate new list')
book_list = ['Seven Habits', 'How to Influence people', 'First Things First', '40X']
new_book_list = book_list[:]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nCreate new list')
del book_list[:]
for i in range(0, len(book_list)):
    print(book_list[i])


print('\nCreate new list with odd number')
book_list = ['1. Seven Habits', '2. How to Influence people', '3. First Things First', '4. 40X']
new_book_list = book_list[0::2]
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print('\nCreate new list with even number')
book_list = ['1. Seven Habits', '2. How to Influence people', '3. First Things First', '4. 40X']
new_book_list = book_list[1::2]
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print('\nCreate new list with throw away')
book_list = ['1. Seven Habits', '2. How to Influence people', '3. First Things First', '4. 40X']
new_book_list = book_list[0:-1:2]
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print('\nCreate new list with throw away')
book_list = ['1. Seven Habits', '2. How to Influence people', '3. First Things First', '4. 40X']
print(book_list[0::2])

