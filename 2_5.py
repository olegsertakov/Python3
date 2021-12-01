my_list = [7, 6, 6, 5, 3, 3, 2]
print('Исходные числа рейтинга =', my_list)
new_num = int(input('Введите новый элемент рейтинга в виде числа от 0 до 9 ='))
print(f'{new_num}')

i = 0                      # задаем начальное значение индекса списка
for n in my_list:
    if new_num <= my_list[i]:
        i += 1
    elif new_num > my_list[i]:
         break

my_list. insert(i, float(new_num))

print(my_list)
