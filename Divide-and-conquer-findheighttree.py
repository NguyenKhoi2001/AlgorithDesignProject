class Node:
    def __init__(self,value,left,right) -> None:
        '''
        value is the value of the node
        left is the left children node
        right is the right children node
        '''
        self.value = value
        self.left = left
        self.right = right

def insertToTree(node,child):
    '''
    node is the root of tree
    children is the node we want to insert
    '''
    if(child.value<node.value):
        if(node.left == None):
            node.left = child
        else:
            insertToTree(node.left,child)
    else:
        if(node.right == None):
            node.right = child
        else:
            insertToTree(node.right,child)
    
def buildTree(newNode,lst):
    '''
    build a tree from the begining
    lst is input list of values for node
    ex: [3,5,1,6,7] 
    '''
    for i in range(1,len(lst)):
        insertToTree(newNode,Node(lst[i],None,None))
    

listofvalue = [10,6,7,5,9,12,20,15,3]
'''
               10
            6       12
          5   7         20
        3       9      15

height = 4
if add 2 and 1 => height is 6
'''
newNode = Node(listofvalue[0],None,None)
buildTree(newNode,listofvalue)
#print(newNode.left.left.left.value) you can try to get the tree value 

def findtreeHeight(node):
    if(node.left == None and node.right == None):
        return 1
    if(node.left == None):
        return 1 + findtreeHeight(node.right)
    elif(node.right == None):
        return 1 + findtreeHeight(node.left) 
    else: #if the node has 2 children then find which way is longer
        leftheight = 1 + findtreeHeight(node.left)
        rightheight = 1 + findtreeHeight(node.right)
        if(leftheight<rightheight):
            return 1 + findtreeHeight(node.right)
        else:
            return 1 + findtreeHeight(node.left)

print(findtreeHeight(newNode))
    

#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import sys
sys.setrecursionlimit(2000000) #so that using recursion with large number is allow

def measure(n):
    newNode = Node(n[0],None,None)
    buildTree(newNode,n)
    start = time.time()
    findtreeHeight(newNode)
    stop = time.time()
    return stop - start

n2 = list(range(0,1000,20))
plt2 = plt
plt.plot(n2,n2)
plt.xlabel('input size')
plt.ylabel('number of execution')
plt2.legend(['n'])
plt.show()

iput = []
for i in n2:
    temp = [0]
    for j in range(i):
        temp.append(j)
    iput.append(temp)
running_time = [measure(x) for x in iput]

plt2.plot(n2,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['find height tree divide and conquer'])
plt2.show()