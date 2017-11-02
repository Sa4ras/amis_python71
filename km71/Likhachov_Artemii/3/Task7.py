print('This program calculate the count of hours and minutes after 00:00')
while True:
    X = input('Input minutes: ')
    try:
        if int(X) >= 0:
            h = int(X)//60
            m = int(X)%60
            print(h, 'hours', m, 'minutes')
            break
        else:
            print('Try again')
            continue
    except ValueError:
        print('Try again')
        continue
print('Artemii Likhachov KM-71')