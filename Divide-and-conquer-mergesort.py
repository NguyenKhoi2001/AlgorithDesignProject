def mergesort(A, i, j):
    '''
    mergesort is sorting list with given starting index i and ending index j
    in merge we divide by 2 smaller and sort again
    '''
    if i == j: return None
    k = (i + j)//2
    mergesort(A,i,k)
    mergesort(A,k+1,j)
    merge(A, i, k, j)
 
def merge(A,i,k,j):
    '''This function is to merge 2 list after sorting
    '''
    B = [0 for _ in range(len(A))]
    p1, p2, p3 = i, k+1, i
    while p1 <= k and p2 <= j:
        if A[p1] < A[p2]:
            B[p3] = A[p1]
            p1 += 1
        else:
            B[p3] = A[p2]
            p2 += 1
        p3 += 1
    while p1 <= k:
        B[p3] = A[p1]
        p3 += 1
        p1 += 1
    while p2 <= j:
        B[p3] = A[p2]
        p3 += 1
        p2 += 1
    for r in range(i, j+1):
        A[r] = B[r]

#test case
newList = [2,5,1,7,8,3,8,8,6]
output = [1,2,3,5,6,7,8,8,8]
mergesort(newList,0,len(newList)-1)
print(newList)
print(output)

#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import copy
import math


def measure(n):
    start = time.time()
    A = mergesort(n,0,len(n)-1)
    stop = time.time()
    return stop - start

n2 = list(range(1,10000,200))
plt2 = plt
plt.plot(n2,[i*math.log(i) for i in n2])
plt.xlabel('input size')
plt.ylabel('number of execution')
plt2.legend(['nlogn'])
plt.show()

iput = []
for i in n2:
    temp = [0]
    for j in range(i):
        temp.append(j)
    iput.append(temp)
running_time = [measure(x) for x in iput]

plt2.plot(n2,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['mergesort divide and conquer'])
plt2.show()