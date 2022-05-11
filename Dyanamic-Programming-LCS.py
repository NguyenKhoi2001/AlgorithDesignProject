def LCS(A,B):
    '''LCS function is to find the Longest Common Subsequence
    with A is first input sentence
    B is second sentence
    '''

    m = len(A)
    n = len(B)

    Len = [[None]*(n+1) for i in range(m+1)] #for computing common subsequnce
    prev = [[None]*(n+1) for i in range(m+1)] #for backtracking

    for i in range(m+1):
        Len[i][0] = 0 #make first column 0 as initialize
    for j in range(n+1):
        Len[0][j] = 0 #make first row 0 as initialize
    #computing LCS
    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                Len[i][j]=Len[i-1][j-1] + 1
                prev[i][j]="topleft"
            elif Len[i-1][j] >= Len[i][j-1]:
                Len[i][j]=Len[i-1][j]
                prev[i][j]="top"
            else:
                Len[i][j]= Len[i][j-1]
                prev[i][j]="left"
    #print("LCS reuslt is: ")
    #outputLSC(A,prev,i,j)
    #print()
    return Len
    
#backtracking to print out the common subsequence
def outputLSC(A,prev,i,j):
    if i==0 or j==0:
        return 
    if prev[i][j]=="topleft":
        outputLSC(A,prev,i-1,j-1)
        print(A[i-1],end = '')
    elif prev[i][j]=="top":
        outputLSC(A,prev,i-1,j)
    else:
        outputLSC(A,prev,i,j-1)

s1 = "president"
s2 = "providence"
output = "priden"
LCS(s1,s2)
print(output)

# LCS(s1,s2)
# LCS(s3,s4)

#time running demo:
import numpy as np
from matplotlib import pyplot as plt
import time
import sys
import random
sys.setrecursionlimit(2000000) #so that using recursion with large number is allow



def measure(n):
    start = time.time()
    A = LCS(n[0],n[1])
    stop = time.time()
    return stop - start

n2 = list(range(0,50))
plt2 = plt



iput = []
xline = []
yline = []
for i in n2:
  a = ''
  b = ''
  for j in range(i): 
    a += 'B'
    b += 'C'
  iput.append([a,b])
  xline.append(len(a)+len(b))
  yline.append(len(a)*len(b))
running_time = [measure(x) for x in iput]
plt.plot(xline,yline)
plt.xlabel('input size')
plt.ylabel('number of execution')
plt2.legend(['n*m where n = m'])
plt.show()

plt2.plot(xline,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['LCS of 2 string where len equal'])
plt2.show()