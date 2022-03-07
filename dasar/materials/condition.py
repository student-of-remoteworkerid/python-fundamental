# Percabangan
milk_bottle_count = 173
egg_count = 1587

print(f'Jumlah botol susu {milk_bottle_count} botol')
print(f'Jumlah telur {egg_count} butir')

if milk_bottle_count > 0:
    print('Budi mengecek harganya, dan ternyata uangnya cukup')
    if egg_count == 0:
        print('Budi membeli 1 botol susu')
    else:
        print('Budi membeli 6 botol susu')
else:
    print('Budi tidak jadi membeli 1 botol susu')

print('Budi pulang ke rumah')
print('menyampaikan hasilnya ke ibunya')

print()

