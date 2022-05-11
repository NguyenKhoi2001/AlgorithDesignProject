def change_making(C,m):
    '''Chang making will comput the minimum coin needed to change
    C is input list of coins value
    m is the input money
    '''
    C.insert(0,0) #insert 0 at the first
    n = len(C) #len c now increase +1
    C.insert(-1,0) #insert -1 at the first
    # if C = [25,10,5,1] now it is C = [-1,0,25,10,5,1]
    F = [(m+1) for i in range(m+1)]
    F[0] = 0
    for i in range(1,m+1):
        temp = m+1
        j = 1
        while j<=n and C[j]<=i: 
            #if put the bigger coin in success then go
            #if not go to next coins and start again
            temp = min(F[i-C[j]],temp)
            j+=1
        F[i] = temp + 1
    return F[m]

#test case
Coins = [25,10,5,1]
money = 49
#output (7: 25 + 10 + 10 + 1 + 1 + 1 + 1 = 49)
output = 7
print(change_making(Coins,money))
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
    A = change_making(n[0],n[1])
    stop = time.time()
    return stop - start

n2 = list(range(0,1000,50))
plt2 = plt


iput = []
xline = []
for j in n2:
  #temp
  temp = [] #list of coin
  for k in range(j):
    temp.append(k)
  iput.append([temp,j+10])
  xline.append([j*len(temp)])


plt.plot(n2,xline)
plt.xlabel('input size')
plt.ylabel('number of execution')
plt2.legend(['n*m where n ~ m'])
plt.show()

running_time = [measure(x) for x in iput]
plt2.plot(n2,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['Change making Dyanmic programming'])
plt2.show()