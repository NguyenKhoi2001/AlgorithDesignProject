class Board:
    def __init__(self, size):
        self.N = size
        self.board = [[0]*size for i in range(self.N)]
    def printSolution(self, board):
        for i in range(self.N):
            for j in range(self.N):
                print (board[i][j], end = " ")
            print()
    

    def isSafe(self, row, col):
        #checking column
        for i in range(self.N):
            if self.board[row][i] == 1 or self.board[i][col] == 1:
                return False
            
        #checking diagonals
        for k in range(self.N):
            for l in range(self.N):
                if (abs(k-l==row-col)):
                    if self.board[k][l]==1:
                        return False
        return True
            
    def solving(self, col):
        '''
        with backtracking queen problem
        we place each queen in each column then go next column
        check if this queen place in this column is crash (by row or diagnose)
        we find another row for this queen
        until we find solution and return it
        if no solution then return false
        '''
        #base case if column is bigger than size stop
        #col bigger than size when all queen has been place
        if col >= self.N: 
            return True
        for i in range(self.N):
            #check the queen placement is good or not
            if self.isSafe(i, col):
                self.board[i][col] = 1
                #after place queen success, go try next column
                if self.solving(col + 1) == True:
                    return True
                
                #if next column is unable to place:
                #meaning it is not the solution so we undo the queen
                self.board[i][col] = 0
            
            #go next row try to place queen
        
        #if the queen cannot be place in anyrow
        #in this column => the solution is wrong
        return False
    def queenSolving(self): 
        if self.solving(0) == False:
            print("no solution")
            return False
        #print was cut out so that running time can be run easy
        #self.printSolution(self.board)
        return True
 


q = Board(5)
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

N = list(range(3,11))

plt2 = plt
def fac(n):
  fact = 1
  for i in range(1,n+1):
      fact = fact * i
  return fact
      
plt.plot(N,[fac(i) for i in N])
plt.xlabel('input size')
plt.ylabel('number of execution')
plt2.legend(['n!'])
plt.show()

running_time = [measure(x) for x in N]
plt2.plot(N,running_time)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['N-queen backtracking'])
plt2.show()