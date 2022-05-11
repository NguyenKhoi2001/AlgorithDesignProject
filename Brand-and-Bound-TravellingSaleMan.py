import math
maxsize = float('inf')
  

def copyToFinal(curr_path):
    '''
    Function to copy temporary solution to the final solution
    '''
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]
  

def firstMin(adj, i):
    '''
    Function to find the minimum edge cost having an end at the vertex i
    proper saying finding min in row
    '''
    min = maxsize #set min to infinity
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]
  
    return min
  
def secondMin(adj, i):
    '''
    function to find the second minimum edge cost having an end at the vertex i
    '''
    temp, min = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= temp:
            min = temp
            temp = adj[i][j]
  
        elif(adj[i][j] <= min):
            min = adj[i][j]
  
    return min
  

def TSPRec(adj, curr_bound, curr_weight, level, curr_path, visited):
    '''function that takes as arguments:
    curr_bound -> lower bound of the root node
    curr_weight-> stores the weight of the path so far
    level-> current level while moving in the search space tree
    curr_path[] -> where the solution is being stored which would later be copied to final_path[]
    '''
    global final_res
    # base case is when we have reached level N 
    # which means we have covered all the nodes once
    if level == N:
          
        # check if there is an edge from
        # last vertex in path back to the first vertex
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
              
            # curr_res has the total weight
            # of the solution we got
            curr_res = curr_weight + adj[curr_path[level - 1]]\
                                        [curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return
  
    # for any other level iterate for all vertices
    # to build the search space tree recursively
    for i in range(N):
          
        # Consider next vertex if it is not same 
        # (diagonal entry in adjacency matrix and 
        #  not visited already)
        if (adj[curr_path[level-1]][i] != 0 and
                            visited[i] == False):
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]
  
            # different computation of curr_bound 
            # for level 2 from the other levels
            if level == 1:
                curr_bound -= ((firstMin(adj, curr_path[level - 1]) + 
                                firstMin(adj, i)) / 2)
            else:
                curr_bound -= ((secondMin(adj, curr_path[level - 1]) +
                                 firstMin(adj, i)) / 2)
  
            # curr_bound + curr_weight is the actual lower bound 
            # for the node that we have arrived on.
            # If current lower bound < final_res, 
            # we need to explore the node further
            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
                  
                # call TSPRec for the next level
                TSPRec(adj, curr_bound, curr_weight, 
                       level + 1, curr_path, visited)
  
            # Else we have to prune the node by resetting 
            # all changes to curr_weight and curr_bound
            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp
  
            # Also reset the visited array
            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True
  
# This function sets up final_path
def TSP(adj):
    '''
    Calculate initial lower bound for the root node 
    using the formula 1/2 * (sum of first min + second min)
    for all edges. Also initialize the curr_path and visited array
    '''  
    curr_bound = 0
    curr_path = [-1 for i in range(N+1)]
    visited = [False] * N
  
    # Compute initial bound
    for i in range(N):
        curr_bound += (firstMin(adj, i) + 
                       secondMin(adj, i))
  
    # Rounding off the lower bound to an integer
    curr_bound = math.ceil(curr_bound / 2)
  
    # We start at vertex 1 so the first vertex 
    # in curr_path[] is 0
    visited[0] = True
    curr_path[0] = 0
  
    # Call to TSPRec for curr_weight 
    # equal to 0 and level 1
    TSPRec(adj, curr_bound, 0, 1, curr_path, visited)
  
# Driver code
  
# test case
adj = [[0, 10, 15, 20],
       [10, 0, 35, 25],
       [15, 35, 0, 30],
       [20, 25, 30, 0]]
'''
out put is 0 1 3 2 0 with total is 80
'''
N = 4
final_path = [None] * (N + 1)# final_path[] stores the final solution 
final_res = maxsize# Stores the final minimum weight
TSP(adj)
print("Minimum cost :", final_res)
print("Path Taken : ", end = ' ')
for i in range(N + 1):
    print(final_path[i], end = ' ')


#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import sys
import random
sys.setrecursionlimit(2000000) #so that using recursion with large number is allow

def measure(n):
    start = time.time()
    global N
    N = len(n)
    final_path = [None] * (N + 1)# final_path[] stores the final solution 
    final_res = maxsize# Stores the final minimum weight
    TSP(n)
    stop = time.time()
    return stop - start

n2 = list(range(5,100,5))


n3 = [i**2 for i in n2]
plt2 = plt
plt.plot(n2,n3)
plt.xlabel('input size')
plt.ylabel('number of execution')
plt.legend(['n^2'])
plt.show()

iput = []
for k in n2:
    temp = [[1]*k for i in range(k)]
    #set diagnose is zero
    for i in range(len(temp)):
      temp[i][i] = 0
    iput.append(temp)
running_time = [measure(x) for x in iput]

plt2.plot(n2,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt.legend(['travelling sale man brand and bound'])
plt2.show()
