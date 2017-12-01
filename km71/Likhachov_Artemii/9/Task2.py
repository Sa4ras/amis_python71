def power(a,n):
    if a <= 0 and not n.isdigit():
        return 'Error'
    res = a
    for i in range(n-1):
        res*=a
    return res

x = float(input())
y = input()
print(power(x,y))