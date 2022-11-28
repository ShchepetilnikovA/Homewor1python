result = None
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x or y or z) != (not x) and  (not y) and (not z):
                result = 0
                break
    
if result:
    print ('выражения несправедливы')
else:
    print ('выражения справедливы')