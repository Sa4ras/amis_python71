print('This program tells you the previous and next number of your number')
while True:
    x = input('Input your number, please ')
    try:
        print('The next number for the number', int(x), 'is', int(x)+1, '\n The previous number for the number', int(x), 'is', int(x)-1)
        break
    except ValueError:
        print('Try again')
        continue
print('Artemii Likhachov KM-71')