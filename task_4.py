number = int(input('введите целое положительное число ='))
number_max = number % 10
number = number // 10
while number > 0:
    number_ost = number % 10
    if number_ost > number_max:
        number_max = number_ost

    number = number // 10

print('максимальное число = ', number_max)