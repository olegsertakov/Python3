vyruchka = float(input('Введите значение выручки = '))
izderzhki = float(input('Введите значение издержек = '))
if vyruchka >= izderzhki:
    pribyl = vyruchka - izderzhki
    print('Прибыль равна = ', pribyl)
    rentabel = pribyl / vyruchka
    personal = int(input('Введите численность персонала фирмы = '))
    pribyl_1 = pribyl / personal
    print('Прибыль на одного сотрудника равна = ', pribyl_1)
else:
    ubytok = izderzhki - vyruchka
    print('Убыток равен = ', ubytok)