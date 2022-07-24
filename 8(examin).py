file = open('9.txt', 'r')
a = 0
mas = file.readlines()
for i in range(len(mas)):
    mas[i] = mas[i].strip().split()
for el in mas:
    if int(el[2]) < 3:
        print(el[0], el[1])
    a += int(el[2])
print('Средний балл по классу:', a / len(mas))
file.close()
