# with For
book_count = 10

print('Mom said, "Read all your book"')
number_of_reads_book = 0

for number_of_reads_book in range(1, book_count + 1):
    print(f'book of {number_of_reads_book} have read')

print(f"report to mom, you have finished read {number_of_reads_book} book")

print()

# with While
book_count = 10

print('Mom said, "Read all your book"')
number_of_reads_book = 0

while number_of_reads_book < book_count:
    number_of_reads_book += 1
    print(f'book of {number_of_reads_book} have read')


print(f"report to mom, you have finished read {number_of_reads_book} book")