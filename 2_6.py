goods = []
options = {'название': ' ', 'цена': ' ', 'количество': ' ', 'единица измерения': ' '}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0

while True:
    if input("Для выхода из приложения нажмите Q, для продолжения Enter: ").upper() == 'Q':
        break
    num += 1
    for f in options.keys():
        prop = input(f'Введите значение свойства {f} -')
        options[f] = int(prop) if f in ('цена', 'количество') else prop
        analitics[f].append(options[f])
        goods.append((num, options.copy()))
    print(f"\nСтруктура товаров\n{goods}")
    print(f"\nТекущая аналитика по товарам\n{'*'*30}")
    for key, value in analitics.items():
        print(f"{key[:25]:>30}: {value}")
    print('*'*30)

