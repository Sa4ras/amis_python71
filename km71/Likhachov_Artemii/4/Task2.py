def function_sign(float):
    if float > 0:
        return 1
    if float == 0:
        return 0
    else:
        return -1

x = float(input('Input number X: '))
print('sign(X) = ',function_sign(x))
