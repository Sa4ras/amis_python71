inputs = input('Input numbers: ').split()
for i in inputs:
    k = inputs.count(i)                                       
    if k == 1:
        print(i)