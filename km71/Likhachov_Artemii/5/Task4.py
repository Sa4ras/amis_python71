N = int(input('Input number of kegels: '))
stay = ['l']*N
K = int(input('Input number of throws: '))
for i in range (K):
    while True:
        li = int(input("Input number of first kegel: "))
        ri = int(input("Input number of last kegel:  "))
        if 1 <= li <= ri <= N:
            for k in range(li, ri+1):
                stay[k-1] = "."
            break
        else:
            print('Must be 1≤ li≤ ri≤ N. Try again.')
            continue
for m in range(len(stay)):
    print(stay[m], end='')