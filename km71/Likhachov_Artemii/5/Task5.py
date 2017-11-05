a = [int(i) for i in input().split()]
ans = (lambda i: bool(i==i+2) or bool(abs(i-(i+2))==abs((i+1)-(i+4))), a)
if ans == True:
    print('YES')
else:
    print('NO')