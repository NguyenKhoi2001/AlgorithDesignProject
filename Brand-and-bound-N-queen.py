class Board:
    def __init__(self, size):
        self.N = size
        self.board = [[0]*self.N for i in range(self.N)]
    def printSolution(self, board):
        for i in range(self.N):
            for j in range(self.N):
                print (board[i][j], end = " ")
            print()
    

    def isSafe(self, row, col, slashCode, backslashCode, 
        rowLookup, slashCodeLookup, backslashCodeLookup):
        #checking column
        if (slashCodeLookup[slashCode[row][col]]):
            return False
        elif backslashCodeLookup[backslashCode[row][col]]:
            return False
        elif rowLookup[row]:
            return False
        return True
            
    def solving(self, col, slashCode, backslashCode, 
        rowLookup, slashCodeLookup, backslashCodeLookup):
        '''
        Solving N-queen problem by using Brand-and-bound method
        '''
        if col >= self.N: #when all queen has been placed
            return True
        for i in range(self.N):
            #check the queen placement is good or not
            if self.isSafe(i, col,slashCode, backslashCode, 
        rowLookup, slashCodeLookup, backslashCodeLookup):
                self.board[i][col] = 1
                rowLookup[i] = True #check row is occupied
                slashCodeLookup[slashCode[i][col]] = True
                backslashCodeLookup[backslashCode[i][col]] = True

                #after place queen success, go try next column
                if self.solving(col + 1,slashCode, backslashCode, 
                rowLookup, slashCodeLookup, backslashCodeLookup) == True:
                    return True
                
                #if next column is unable to place:
                #meaning it is not the solution so we undo the queen
                self.board[i][col] = 0
                rowLookup[i] = False
                slashCodeLookup[slashCode[i][col]] = False
                backslashCodeLookup[backslashCode[i][col]] = False
            
            #go next row try to place queen
        
        #if the queen cannot be place in anyrow
        #in this column => the solution is wrong
        return False
    def queenSolving(self):

        #create slashBoard and backslashboard
        slashCode = [[0 for j in range(self.N)] for i in range(self.N)]
        backslashCode = [[0 for j in range(self.N)] for i in range(self.N)]

        # keep two arrays to tell us
        # which diagonals are occupied
        x = 2 * self.N - 1
        slashCodeLookup = [False] * x
        backslashCodeLookup = [False] * x

        # arrays to tell us which rows are occupied
        rowLookup = [False] * self.N
        # initialize helper matrices
        for rr in range(self.N):
            for cc in range(self.N):
                slashCode[rr][cc] = rr + cc
                backslashCode[rr][cc] = rr - cc + self.N-1
        if(self.solving(0, slashCode, backslashCode,
                        rowLookup, slashCodeLookup,
                        backslashCodeLookup) == False):
            print("no solution")
            return False

        '''
        This row was commented so that running time can run easy
        #self.printSolution(self.board)
        '''
        return True


#test case
q = Board(5)
'''
output:
Q . . . . 
. . . Q .
. Q . . .
. . . . Q
. . Q . .
'''
print(q.queenSolving())


#time running function
import time
import random
from matplotlib import pyplot as plt
def measure(N):
    """
    ...
    """
    start = time.time()
    q = Board(N)
    q.queenSolving()
    stop = time.time()
    return stop - start

N = list(range(3,21))

plt2 = plt
def fac(n):
  fact = 1
  for i in range(1,n+1):
      fact = fact * i
  return fact
      
plt.plot(N,[fac(i) for i in N])
plt.xlabel('input size')
plt.ylabel('number of execution')
plt.legend(['n!'])
plt.show()

running_time = [measure(x) for x in N]
plt2.plot(N,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['N-queen brand and bound'])
plt2.show()