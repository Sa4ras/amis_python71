x1 = int(input('Input x1: '))
x2 = int(input('Input x2: '))
x3 = int(input('Input x3: '))
txt = 'Bigger number is: '
if x1 > x2 and x1 > x3:
    print(txt, x1)
if x2 > x1 and x2 > x3:
    print(txt, x2)
else:
    print(txt, x3)

