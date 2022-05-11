#Ford-Fulkerson Algorithm
#find path by using BFS
def dfs(graph, F, s, t):
        stack = [s]
        paths={s:[]}
        if s == t:
                return paths[s]
        while(stack):
                u = stack.pop()
                for v in range(len(graph)):
                        if(graph[u][v]-F[u][v]>0) and v not in paths: #basic operation
                                paths[v] = paths[u]+[(u,v)]
                                if v == t:
                                        return paths[v]
                                stack.append(v)
        return None

def max_flow(graph, s, t):
        n = len(graph) 
        F = [[0] * n for i in range(n)] #F is the flow
        path = dfs(graph, F, s, t)
        while path != None: #you can write like while dfs(graph,F,s,t) for short
            flow = min(graph[u][v] - F[u][v] for u,v in path)
            for u,v in path:
                F[u][v] += flow
                F[v][u] -= flow
            path = dfs(graph,F,s,t)
        return sum(F[s][i] for i in range(n))
    
#test case
mygraph = [[0,3,2,0],
        [0,0,3,2],
        [0,0,0,3],
        [0,0,0,0]]
source = 0
sink = 3  
outputflow = 5 #3 from 0-1 and 2 from 0-2 
max_flow_value = max_flow(mygraph, source, sink)
print("max_flow_value is: ", max_flow_value)
print(outputflow)

#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import sys
import random
sys.setrecursionlimit(2000000) #so that using recursion with large number is allow



def measure(n):
    start = time.time()
    A = max_flow(n,0,len(n)-1)
    stop = time.time()
    return stop - start

n2 = list(range(5,50))


plt2 = plt
plt.plot(n2,[i*random.randint(i,i+20) for i in n2])
plt.xlabel('input size')
plt.ylabel('number of execution')
plt2.legend(['n*random max flow'])
plt.show()

iput = []
for i in n2:
  newGraph = [[random.randint(1,20) for j in range(i)] for k in range(i)]
  #to make directed graph change some value to 0
  lenG = len(newGraph)
  for k in range(lenG):
    for l in range(k+1):
      newGraph[k][l] = 0 
  iput.append(newGraph)
running_time = [measure(x) for x in iput]
plt2.plot(n2,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['Forfulker son with E increase and random maxflow'])
plt2.show()
