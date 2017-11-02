def correct_input(int):
    if int>8 or int<1:
        return 1
    else:
        return 0

def black_point(a1, a2):
    if a1==a2 or a1%2==a2%2:
        return 1
    else:
        return 0

def white_point(b1, b2):
    if b1!=b2 or b1%2!=b2%2:
        return 1
    else:
        return 0

a1 = int(input('Start position in row: '))
a2 = int(input('Start position in column: '))
b1 = int(input('Second position in row: '))
b2 = int(input('Second position in column: '))
if correct_input(a1) or correct_input(a2) or correct_input(b1) or correct_input(b2):
    print('Error')
elif black_point(a1, a2) is 1 and white_point(b1, b2) is 0:
    print('YES')
elif black_point(a1, a2) is 0 and white_point(b1, b2) is 1:
    print('YES')
else:
    print('NO')
