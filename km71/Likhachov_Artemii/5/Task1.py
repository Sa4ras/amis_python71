answer = 'Growth can not be bigger than 200. Try again'
while True:
    pupils = [int(i) for i in input('Pupils growth: ').split(' ')]
    for i in pupils:
        if i <=200:
            break
        else:
            print(answer)
            continue
    petya = int(input('Petyas growth: '))
    if petya <= 200:
        break
    else:
        print(answer)
        continue
position = 1
for i in pupils:
    if i >= petya:
        position += 1
print('His position:', position)