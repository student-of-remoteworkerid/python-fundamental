# with For
book_count = 10

print('Mom said, "Read all your book"')
read_count = 0

for read_count in range(1, book_count + 1):
    print(f'book of {read_count} has been read')

print(f"report to mom, you has been finished read all {read_count} book")

print()

# with While
book_count = 10

print('Mom said, "Read all your book"')
read_count = 0

while read_count < book_count:
    read_count += 1
    print(f'book of {read_count} has been read')

print(f"report to mom, you has been finished read all {read_count} book")

print()

# with While Undefined Count

book_count = 10
print('Mom said "Read all the books until you understand"')
read_count = 0

understood_count = 0
print(f'number of books read and understood {understood_count}')

while read_count < book_count * 2:
    read_count += 1
    if understood_count == 9:
        print(f'book of {understood_count + 1} not understood')
    else:
        understood_count += 1
        print(f'book of {understood_count} has been read and understood')

print(f"number of books you read and understood {understood_count} book")
if understood_count == book_count:
    print('report to mom, all books have been read and understood')
else:
    print(f"report to mom, not all books can be understood. "
          f" Budi can only understand {understood_count} book")
