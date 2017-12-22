def sec_max_element(A):
    if len(A) == 2:
        A.sort(reverse=True)
        return A[1]
    elif len(A) == 3:
        A.sort(reverse=True)
        if A[0]==A[1]:
            return A[2]
        return A[1]
    else:
        A.sort(reverse=True)
        return sec_max_element(A[1:])

list = input().split()

print(sec_max_element(list))

