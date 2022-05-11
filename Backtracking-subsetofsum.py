class Node:
    def __init__(self, value, parent, select) -> None:
        """
        creates a node containing value(int), reference to parent node(Node), select(int)
        input:
        value(int): sum of partial subset
        parent(Node): reference to parent node
        select(int): index of the node in the original set (represented as a list), or 
        -1 if the node is not selected
        output:
        a node (Node)
        """
        self.value = value
        self.parent = parent
        self.select = select
    
def print_combination(node, S):
    if node.parent:
        if node.select >=0:
            print(f"{S[node.select]}", sep="-")
        print_combination(node.parent,S)
 

def sum_of_subset(node, S, d, index):
    if node.value == d:
        '''
        #this print is commented for analysis running time
        #if you want result uncomment the print
        print_combination(node, S)
        '''
    elif(node.value < d) and (index < len(S)) and (node.value + sum(S[index:]) >= d):
        next_element = S[index]
        child = Node(node.value + next_element, node, index)
        #backtracking
        sum_of_subset(child, S, d, index + 1)
        child = Node(node.value, node, -1)
        sum_of_subset(child, S, d, index + 1)
    
#test case
list1 = [3,5,6,7]
target = 15
'output = 3+5+7'
node0 = Node(0,None,0)
sum_of_subset(node0, list1, target, 0)

#time running function
import time
import random
from matplotlib import pyplot as plt
def measure(N):
    """
    ...
    """
    start = time.time()
    newNode = Node(0,None,0)
    sum_of_subset(newNode,N,len(N)+5,0)
    stop = time.time()
    return stop - start

N = list(range(3,50,5))

plt2 = plt
      
plt.plot(N,[2**i for i in N])
plt.xlabel('input size')
plt.ylabel('number of execution')
plt2.legend(['2^n'])
plt.show()

iput = []
for i in N:
  temp = []
  for j in range(i):
    temp.append(j)
  iput.append(temp)

running_time = [measure(x) for x in iput]

plt2.plot(N,running_time)
plt2.xlabel('input size')
plt2.ylabel('number of execution')
plt2.legend(['sum of sub set backtracking'])
plt2.show