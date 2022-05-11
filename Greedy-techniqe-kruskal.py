def sortingEdges(graph):
    #sorting using bruteforce method
    
    for i in range(len(graph)):
        min = graph[i][2]
        index = i #initial index of min edge
        for j in range(i+1,len(graph)): # find max
            if min > graph[j][2]:
                min = graph[j][2]
                index = j
        #switch max to the front
        graph[i],graph[index] = graph[index],graph[i]
    return graph

def find(parent, i):
    '''function to find set of an element i'''
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
 
        # Attach smaller rank tree under root of high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # If ranks are same, then make one as rootand increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

def KruskalMST(graph):
    '''KrusalMST will find minimum spaning tree with input adjacency matrix
    '''
    #stop duplicate (1 -- 4, w: 6 the same with 4 -- 1, w: 6)
    #we stop by do u -- v with u < v (u is start vertice and v is end vertice)
    newGraph = []
    for i in range(len(graph)):
        for j in range(i,len(graph)):
            if graph[i][j] != 0:
                #add edge follow this format [u,v,w]
                newGraph.append([i,j,graph[i][j]]) 

    #sorting edges in non-decreasing of the weight
    newGraph = sortingEdges(newGraph)

    parent = []
    rank = []
    V = len(graph) #number of vertices
    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)

    result = [] #store the result
    #create 2 index variable for loop
    i = 0 #i is for sorting edge,
    e = 0 #e is for result[]

    # Number of edges to be taken is equal to V-1
    while e < V - 1:
 
        # Step 2: Pick the smallest edge and increment
        # the index for next iteration
        u, v, w = newGraph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
 
        # If including this edge does't
        #  cause cycle, include it in result
        #  and increment the indexof result
        # for next edge
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
        # Else discard the edge

    #print the tree
    minimumCost = 0
    print ("Edges in the constructed MST")
    for u, v, weight in result:
        minimumCost += weight
        #print("%d -- %d == %d" % (u, v, weight))
    print("Minimum Spanning Tree" , minimumCost)

#testcase
myGraph = [[0,4,0,0,0,0,0,8,0],
            [4,0,8,0,0,0,0,11,0],
            [0,8,0,7,0,4,0,0,2],
            [0,0,7,0,9,14,0,0,0],
            [0,0,0,9,0,10,0,0,0],
            [0,0,7,14,10,0,2,0,0],
            [0,0,0,0,0,2,0,1,6],
            [8,11,0,0,0,0,1,0,7],
            [0,0,2,0,0,0,6,7,0]]
KruskalMST(myGraph)

#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import sys
import random
sys.setrecursionlimit(2000000) #so that using recursion with large number is allow

def measure(n):
    start = time.time()
    KruskalMST(n)
    stop = time.time()
    return stop - start

n2 = list(range(5,20,1))
n3 = [i**2 for i in n2]
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
plt.legend(['Kruskal minimum spanning tree Greedy technique'])
plt2.show()