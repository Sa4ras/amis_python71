def power(a,n):
    if n == 0:
        return 1
    if n == 1:
        return a
    else:
        return a*power(a, n-1)




x = int(input('A=' ))
y = int(input('n='))
print(power(x,y))