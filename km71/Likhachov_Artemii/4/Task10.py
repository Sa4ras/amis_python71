import math

def correct_input(int):
    if int>8 or int<1:
        return 1
    else:
        return 0

a1 = int(input('Start position in row: '))
a2 = int(input('Start position in column: '))
b1 = int(input('Second position in row: '))
b2 = int(input('Second position in column: '))
if correct_input(a1) or correct_input(a2) or correct_input(b1) or correct_input(b2):
    print('Error')
elif a1==b1 or a2==b2 or abs(a1-b1)==abs(a2-b2):
    print('YES')
else:
    print('NO')