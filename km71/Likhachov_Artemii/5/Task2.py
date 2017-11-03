inputs = input('Input numbers: ').split()
count=0
for i in inputs:
    for u in inputs:
        if i == u:
            count += 1
print('Count of special numbers: ', count - len(inputs))