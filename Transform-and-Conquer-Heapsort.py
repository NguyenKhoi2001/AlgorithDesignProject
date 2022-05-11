def max_heapify(ls, heap_size,i):
    """This operation is also sometimes called "push down", "shift_down" or
    "bubble_down".

    Time complexity: O(log(n))."""
    m = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heap_size and ls[left] > ls[m]:
        m = left
    if right < heap_size and ls[right] > ls[m]:
        m = right
    if i != m:
        ls[i], ls[m] = ls[m], ls[i]
        max_heapify(ls, heap_size, m)


def build_max_heap(ls):
    """
    this function is create a heap 
    Time complexity: O(n)
    """
    for i in range(len(ls) // 2, -1, -1):
        max_heapify(ls, len(ls), i)


def heap_sort(ls):
    build_max_heap(ls)
    for i in range(len(ls) - 1, 0, -1):
        ls[i], ls[0] = ls[0], ls[i]
        max_heapify(ls, i, 0)

#test case
newList = [3,2,5,7,4,7,9]
output = [2,3,4,5,7,7,9]
heap_sort(newList)
print(newList)
print(output)

#time running function
import time
from matplotlib import pyplot as plt
import math
def measure_time(func, N):
    """
    ...
    """
    runtime = []
    for n in N:
        start = time.time()
        func(n)
        stop = time.time()
        runtime.append(stop-start)
    return runtime

N = list(range(1,20000,500)) 

plt2 = plt
n2 = [i*math.log(i) for i in N]
plt.plot(N,n2)
plt.xlabel('input size')
plt.ylabel('time running in second')
plt2.legend(['nlogn'])
plt.show()
iput = []
for i in range(5,len(N)+5):
    iput.append(list(range(i)))
rtime = measure_time(heap_sort,iput)
plt2.plot(N,rtime)
plt2.xlabel('input size')
plt2.ylabel('time running in second')
plt2.legend(['heapsort Transform and conquer'])
plt2.show()