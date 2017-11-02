print('This program calculate the count of apples for each student')
while True:
    N = input('Input a number of students: ')
    K = input('Input a number of apples: ')
    try:
        if  int(N) <= int(K) and int(N) > 0 and int(K) > 0:
            print('Each student get ', int(K)//int(N), 'apples \n', int(K)%int(N), 'left in the box')
            break
        else:
            print('Try again')
            continue
    except ValueError:
        print('Try again')
        continue
print('Artemii Likhachov KM-71')