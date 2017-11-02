import math
print('This program calculate the count of desks')
while True:
    p1 = input('Pupils in first form: ')
    p2 = input('Pupils in second form: ')
    p3 = input('Pupils in third form: ')
    try:
        if int(p1)>0 and int(p2)>0 and int(p3)>0:
            d = math.ceil(int(p1)/2) + math.ceil(int(p2)/2) + math.ceil(int(p3)/2)
            print('You need', d, 'desks')
            break
        else:
            print('Try again')
            continue
    except ValueError:
        print('Try again')
        continue
print('Artemii Likhachov KM-71')