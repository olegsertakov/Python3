
number_max = input('Введите целое число: ')
number = number_max
i = 1
sum = 0
while i <= int(number_max):

    number = int(str(number_max) * i)
    print(number)
    sum = sum + number
    print('текущая сумма чисел = ', sum)
    i += 1
print('сумма ', number_max, 'чисел = ', sum)





