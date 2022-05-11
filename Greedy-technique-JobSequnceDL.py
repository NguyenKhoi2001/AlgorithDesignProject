def totalprofit(A):
    "sum all profit"
    total = 0
    for i in range(len(A)):
        total = total + A[i][2]
    return total

def sortJob(A):
    #A is the list of job with name,deadline,profit
    #ex: (A,3,6),(B,2,1),(C,2,8)
    for i in range(len(A)):
        for j in range(i,len(A)):
            if(A[i][2]<A[j][2]):
                A[i],A[j] = A[j],A[i]

    return A
    #time complexity 0(n^2)



def findMaxdeadline(A):
    "find the maximum deadline"
    max = A[0][1]
    for i in range(len(A)):
        if max < A[i][1]:
            max = A[i][1]
    return max


def jobSequencing(A): 
    A = sortJob(A) #sort the job from highest profit
    result = [(0,0,0)]*findMaxdeadline(A) #store chosen job

    for i in range(len(A)):
        j = A[i][1] - 1 #index for result base on deadline
        while(result[j]!=(0,0,0) and j>-1):
            #if result is occupied and still have index
            #we shift index until free space to store result
            j=j-1
        #store the reuslt in free space if all space is occupy we go next job
        if(j>=0 and result[j]==(0,0,0)):
            result[j] = A[i]
        else:
            continue
    return result #or return totalprofit(result)

#test case
listofJob = [(1,9,2),(2,2,2),(3,5,18),(4,7,1),(5,4,25),(6,2,20),(7,5,8),(8,7,10),(9,4,12),(10,3,5)]
output = [(7,5,8),(6,2,20),(9,4,12),(5,4,25),(3,5,18),(4,7,1),(8,7,10),(0,0,0),(1,9,2)]
print(jobSequencing(listofJob))
print(output)


#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import sys
import random
sys.setrecursionlimit(2000000) #so that using recursion with large number is allow

def measure(n):
    start = time.time()
    A = jobSequencing(n)
    stop = time.time()
    return stop - start

n2 = list(range(2,1000,50))
print(n2)
n3 = [i**2 for i in n2]
plt2 = plt
plt.plot(n2,n3)
plt.xlabel('input size')
plt.ylabel('number of execution')
plt.show()

iput = []
for k in n2:
    temp = []
    for i in range(1,k):
        profit = random.randint(1,i+5)
        deadline = random.randint(1,i+5)
        temp.append((i,deadline,profit))
    iput.append(temp)
running_time = [measure(x) for x in iput]

plt2.plot(n2,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.show()