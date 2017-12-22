#!/usr/bin/python

def minimum(A):
    if len(A) == 1:
        return A[0]
    else:
        A.sort()
        return minimum(A[:1])

a = input().split()
print(minimum(a))

