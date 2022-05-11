def BFsorting(lst):
    '''
    this brute force sorting function will sort a list in ascending order
    (this algorithm called selection sort)
    '''
    for i in range(len(lst)-1):
        min = lst[i]
        for j in range(i+1,len(lst)):
            if min > lst[j]:
                min = lst[j]
                lst[j],lst[i] = lst[i],lst[j]

    return lst

#test case
newList = [6,1,2,9,4,7,3]
output = [1,2,3,4,6,7,9]
print(BFsorting(newList))
print(output)

#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time

def measure(n):
    start = time.time()
    BFsorting(n)
    stop = time.time()
    return stop - start

n2 = list(range(0,10000,500))
print(n2)
n3 = [i**2 for i in n2]
plt2 = plt
plt.plot(n2,n3)
plt.xlabel('input size')
plt.ylabel('number of execution')
plt2.legend(['n^2'])
plt.show()

iput = []
for i in n2:
    temp = [0]*i
    iput.append(temp)
running_time = list(map(measure,iput))

plt2.plot(n2,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['buublesort'])
plt2.show()
