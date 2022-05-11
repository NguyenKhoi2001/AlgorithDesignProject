def BFsearch(lst,key):
    '''
    This brute force search function is to search
    a key in a list and return its index
    Time complexity: n with n is list size
    '''

    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return None

#test case
lst = [1,5,2,8,3,7,9]
key = 8
output = 3
print(BFsearch(lst,key))
print(output)

#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import copy

def measureBF(n):
    start = time.time()
    A = BFsearch(n,-1)
    stop = time.time()
    return stop - start

n2 = list(range(0,10000,200))
plt2 = plt
plt.plot(n2,n2)
plt.xlabel('input size')
plt.ylabel('number of execution')
plt.legend(['n'])
plt.show()

iput = []
for i in n2:
    temp = [0]
    for j in range(i):
        temp.append(j)
    iput.append(temp)
running_time = [measureBF(x) for x in iput]

plt2.plot(n2,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['brute-force search'])
plt2.show()