# with For
book_count = 10

print('Mom said, "Read all your book"')
number_of_books_read = 0

for number_of_books_read in range(1, book_count + 1):
    print(f'book of {number_of_books_read} has been read')

print(f"report to mom, you has been finished read all {number_of_books_read} book")

print()

# with While
book_count = 10

print('Mom said, "Read all your book"')
number_of_books_read = 0

while number_of_books_read < book_count:
    number_of_books_read += 1
    print(f'book of {number_of_books_read} has been read')


print(f"report to mom, you has been finished read all {number_of_books_read} book")

# with While Undefined Count
book_count = 10

print('Mom said "Read all the books until you understand"')

number_of_books_read_and_understood = 0
print(f'number of books read and understood {number_of_books_read_and_understood}')

total_number_of_reads = 0

while total_number_of_reads < book_count * 2:
    total_number_of_reads += 1
    if number_of_books_read_and_understood == 9:
        print(f'book of {number_of_books_read_and_understood + 1} not understood')
    else:
        number_of_books_read_and_understood += 1
        print(f'book of {number_of_books_read_and_understood} has been read and understood')


print(f"number of books you read and understood {number_of_books_read_and_understood} book")
if number_of_books_read_and_understood == book_count:
    print('report to mom, all books have been read and understood')
else:
    print(f"report to mom, not all books can be understood. "
          f" Budi can only understand {number_of_books_read_and_understood} book")