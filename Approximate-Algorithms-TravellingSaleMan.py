from itertools import permutations
maxsize = float('inf')
V = 4
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
 
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost)
        current_pathweight = 0
 
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
 
        # update minimum
        min_path = min(min_path, current_pathweight)
         
    return min_path
 
 
 
# matrix representation of graph
graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]
start = 0
'''
out put way go: 0 - 1 - 3 - 2 - 0 total is 80
'''
print(travellingSalesmanProblem(graph, start))
graph2 = [[0, 10, 15, 20,0], [10, 0, 35, 25,0],
            [15, 35, 0, 30,15], [20, 25, 30, 0,30]
            ,[0,0,15,30,0]]


#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import sys
import random
sys.setrecursionlimit(2000000) #so that using recursion with large number is allow

def measure(n):
    start = time.time()
    global V
    V = len(n)
    travellingSalesmanProblem(n,0)
    stop = time.time()
    return stop - start

n2 = list(range(5,10,1))

def fac(n):
  if n==1:
    return 1
  return n*fac(n-1)

n3 = [fac(i) for i in n2]
plt2 = plt
plt.plot(n2,n3)
plt.xlabel('input size')
plt.ylabel('number of execution')
plt.legend(['n^2'])
plt.show()

iput = []
for k in n2:
    temp = [[0]* k for l in range(k)]
    for i in range(k):
      for j in range(i+1):
        m = random.randint(1,10)
        temp[i][i-j-1] = m
        temp[i-j-1][i] = m
      temp[i][i] = 0
    iput.append(temp)

running_time = [measure(x) for x in iput]

plt2.plot(n2,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt.legend(['travelling sale man brand and bound'])
plt2.show()