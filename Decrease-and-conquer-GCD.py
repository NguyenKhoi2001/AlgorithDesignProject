def findGCD(a,b):
    """find greatest common divisor of 2 number a b"""
    if(b==0):
        return a
    else:
        return findGCD(b,int(a%b))

a = 68
b = 18        
result = findGCD(a,b)
output = 4
print(result)
print(output)

#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import copy
import math

def measure(n):
    start = time.time()
    A = findGCD(n[0],n[1])
    stop = time.time()
    return stop - start

    
n2 = list(range(5,30)) # list of fibonacii number
plt2 = plt

def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


listofFibon = []
for i in range(1,n2[-1]+2):
  listofFibon.append(Fibonacci(i))

print(listofFibon)
print(len(listofFibon))
iput = []
realN= []
for i in n2:
  a = listofFibon[i]
  b = listofFibon[i-1]
  realN.append(a+b)
  iput.append([a,b])

plt.plot(realN,[math.log(i) for i in realN])
plt.xlabel('input size')
plt.ylabel('number of execution')
plt.legend(['log(a+b)'])
plt.show()



running_time = [measure(x) for x in iput]

plt2.plot(realN,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['GCD divide and conquer'])
plt2.show()
