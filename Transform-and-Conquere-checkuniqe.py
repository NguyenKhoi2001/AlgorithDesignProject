def checkUniqueness(A):
    '''
    This function is to check the unique ness of all element in given a list A
    in this case it is into brute-force method
    '''
    for i in range(len(A)-1):
        #check each element is it the same with the rest
        for j in range(i+1,len(A)):
            if(A[i]==A[j]):
                #return immediately if it is duplicate
                return False
    return True
    


#sortting mergesort code
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
 
def presortCheckUnique(A):
    '''
    Transforming to another method for better
    '''
    mergesort(A,0,len(A)-1) #complexity of sorting is O(nlogn)
    #[5,3,7,9,4,3,2,1] => [1,2,3,3,4,5,7,9]
    #duplicate element are next to each other 
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            return False
    return True

#testcase
newList = [3,1,6,8,3,9,0]
output = False #3 is duplicate
print(checkUniqueness(newList))
print(presortCheckUnique(newList))
print(output)

#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import sys
import math
sys.setrecursionlimit(2000000) #so that using recursion with large number is allow

def measure(n):
    start = time.time()
    presortCheckUnique(n)
    stop = time.time()
    return stop - start

def measureBF(n):
    start = time.time()
    checkUniqueness(n)
    stop = time.time()
    return stop - start

n2 = list(range(1,10000,500))
n3 = [i*math.log(i) for i in n2]
plt2 = plt
plt.plot(n2,n3)
plt.xlabel('input size')
plt.ylabel('number of execution')
plt2.legend(['nlogn'])
plt.show()

iput = []
for i in n2:
    temp = []
    for j in range(i,-1,-1):
      temp.append(j)
    iput.append(temp)
running_time = list(map(measure,iput))
running_time_BF = list(map(measureBF,iput))
plt2.plot(n2,running_time,label="transform and conquer")
plt2.plot(n2,running_time_BF,label="brute-force")
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['presort','no presort (bruteforce)'])
plt2.show()
    
