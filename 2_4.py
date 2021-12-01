test_string = input('Введите слова через пробелы -').split()
print(test_string)
'''Вариант вывода № 1'''
for num, val in enumerate(test_string, 1):
    print(str(num), str(val[:10]))
'''Вариант вывода № 2'''
for num, val in enumerate(test_string, 1):
    print(f'{num} {val[:10]}')