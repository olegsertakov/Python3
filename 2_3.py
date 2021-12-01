""" Вариант со списками"""

month = int(input('Введите месяц в виде числа от 1 до 12 ='))
print(month)

season_winter = [1, 2, 12]
season_spring = [3, 4, 5]
season_summer = [6, 7, 8]
season_autumn = [9, 10, 11]

if ((month) in season_winter):
    print('зима')
elif ((month) in season_spring):
    print('весна')
elif ((month) in season_summer):
    print('лето')
else:
    print('осень')

""" Вариант со словарем"""

month = int(input('Введите месяц в виде числа от 1 до 12 ='))
print(month)
seasons = {0:'зима', 1:'весна', 2:'лето', 3:'осень', 4:'зима'}
if 1 <= month <= 12:
    print(seasons[month//3])
else: print('error')
