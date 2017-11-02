m = int(input('Plate width: '))
n = int(input('Plate height: '))
k = int(input('Count of squares in one part: '))

if k/m>=1 or k/n>=1:
    print('YES')
else:
    print('NO')