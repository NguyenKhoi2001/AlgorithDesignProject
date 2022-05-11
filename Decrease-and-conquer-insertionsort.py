def insertSortRecursive(A,n): 
    '''
    A is input array and n is len(A)
    this function is to sort an array
    '''
    if n <= 1:
        return
    insertSortRecursive(A,n-1)
    v = A[n-1] #get the last index
    j = n-2
    while(j>=0 and A[j] > v):
        A[j+1] = A[j]
        j = j - 1
    A[j+1] = v

#test case
A = [5,2,8,3,9,6,8,4,2,1]
output = [1,2,2,3,4,5,6,8,8,9]
insertSortRecursive(A,len(A))
print(A)
print(output)

#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import sys
sys.setrecursionlimit(2000000) #so that using recursion with large number is allow

def measure(n):
    start = time.time()
    insertSortRecursive(n,len(n))
    stop = time.time()
    return stop - start

n2 = list(range(0,10000,500))
print(n2)
n3 = [i**2 for i in n2]
plt2 = plt
plt.plot(n2,n3)
plt.xlabel('input size')
plt.ylabel('number of execution')
plt.legend(['n^2'])
plt.show()

iput = []
for i in n2:
    temp = []
    for j in range(i,-1,-1):
      temp.append(j)
    iput.append(temp)
running_time = list(map(measure,iput))

plt2.plot(n2,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['Insertion sort decrease an conquer'])
plt2.show()