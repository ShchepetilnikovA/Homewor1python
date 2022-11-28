day = int(input('введите номер дня недели: '))
if day > 7 or day <= 0:
    print('day don\'t exist' )
else:
    if day > 5:
        print('weekend')
    else:
        print('weekday')