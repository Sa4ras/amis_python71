x1 = int(input('Input first number: '))
x2 = int(input('Input second number: '))
x3 = int(input('Input third number: '))
if x1==x2==x3:
    print(3)
elif x1==x2!=x3 or x1!=x2==x3 or x1==x3!=x2:
    print(2)
else:
    print(0)
