x = int(input('введите абсциссу: '))
y = int(input('введите ординату: '))
if x == 0 or y == 0:
    print('недопустимое значение')
else:
    if y > 0 and x > 0:
        print('первая четверть')
    elif y > 0 and x < 0:
        print('вторая четверть')
    elif y < 0 and x < 0:
        print('третья четверть')
    elif y < 0 and x > 0:
        print('четвертая четверть')
    