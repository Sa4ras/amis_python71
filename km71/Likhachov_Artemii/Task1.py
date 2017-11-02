print('With this program you can calculate the sum of three numbers')
while True:
    x = input('Input first number: ')
    y = input('Input second number: ')
    z = input('Input third number: ')
    try:
        print('Sum =', x, '+', y, '+', z, '=', float(x)+float(y)+float(z))
        break
    except ValueError:
        print('Try with numbers')
        continue
print('Artemii Likhachov KM-71')