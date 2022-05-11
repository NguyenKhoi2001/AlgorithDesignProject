class Board:
    def __init__(self, size):
        self.N = size
        self.queens = [] # list of columns, where the index represents the row

    def is_queen_safe(self, row, col):
        for r, c in enumerate(self.queens):
            #check in same row/column/diagnose
            if r == row or c == col or abs(row - r) == abs(col - c):
                '''
                  1 2 3 4 
                1 Q
                2 
                3     Q
                4
                '''
                return False
        return True

    def print_the_board(self):
        print ("solution:")
        for row in range(self.N):
            line = ['.'] * self.N
            if row < len(self.queens):
                line[self.queens[row]] = 'Q'
            print(''.join(line))

    def solution(self):
        self.queens = []
        col = row = 0
        while True:
            #check is the position good to place queen
            while col < self.N and not self.is_queen_safe(row, col):
                #if the full column is unable to place go next column
                col += 1
            #if column is till in size of board
            if col < self.N:
                self.queens.append(col)
                #if row is over than board size
                #place complete
                if row + 1 >= self.N: 
                    #this print solution was commented to run the running time
                    #self.print_the_board() 
                    self.queens.pop()
                    col = self.N
                else:
                    row += 1
                    col = 0
            if col >= self.N:
                # not possible to place a queen in this row anymore
                if row == 0:
                    return # all combinations were tried
                col = self.queens.pop() + 1
                row -= 1

#test case
q = Board(4)
'''
output = 
. Q . .
. . . Q
Q . . .
. . Q .
'''
q.solution()


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
    q.solution()
    stop = time.time()
    return stop - start

N = list(range(3,10))

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
plt2.legend(['N-Queen iterative'])
plt2.show()