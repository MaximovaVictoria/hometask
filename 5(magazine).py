count = 0
product = {'торт': ['творог', 'изюм', 5, 100],  # 1-цена, 2-кол-во
           'пирожное': ['крем', 'масло', 7, 120],
           'маффин': ['сахар', 'масло', 9, 140]}
print(
    '''Выберите действие, которое нужно осуществить: *описание; *цена; *количество; *вся информация; *приступить к покупке''')
a = input()
if a == 'описание':
    for key, value in product.items():
        print(key, '-', value[0], ',', value[1])
if a == 'цена':
    for key, value in product.items():
        print(key, '-', value[2], 'рублей')
if a == 'количество':
    for key, value in product.items():
        print(key, '-', value[3])
if a == 'вся информация':
    for key, value in product.items():
        print(key, '-', value[0], ',', value[1], '-', value[2], 'рублей,', value[3])
while True:
    if a == 'приступить к покупке':
        b = input('Введите название продукта')
        if b == 'n' or b not in product:
         break
        c = int(
            input('Введите количество'))  ## посчитать цену выбранных товаров и сколько товаров осталось в изнач. списке
        if c >= product[b][3]:
         print(f'У нас нету {b} в таком большом количестве')
         continue
        count += c * product[b][2]  # колич*цену вся цена
        product[b][3] -= c  # в изнач списке - кол-во которое ввели
print(count)
for key, value in product.items():
    print(key, '-', value[0], '-', value[1], value[2], 'рублей', value[3], 'штук')
