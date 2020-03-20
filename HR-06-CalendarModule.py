from calendar import weekday

date = list(map(int, input().split()))

daynum = weekday(date[2], date[0], date[1])
if 2000 < date[2] < 3000:
    if daynum == 0:
        print('MONDAY')
    elif daynum == 1:
        print('TUESDAY')
    elif daynum == 2:
        print('WEDNESDAY')
    elif daynum == 3:
        print('THURSDAY')
    elif daynum == 4:
        print('FRIDAY')
    elif daynum == 5:
        print('SATURDAY')
    else:
        print('SUNDAY')
