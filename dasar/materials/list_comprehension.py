print('\nList Comprehension')
book_list = ['Seven Habits', 'How to Influence people', 'First Things First', '40X']
new_list = [x for x in book_list if "i" in x]
print(new_list)