
import random
from quick_sort import QuickSort as quick
from radix_sort import RadixSort as radix
import time

n = [n for n in range(10000)]
random.shuffle(n)

quick_sort = quick(n)

t = time.time()
quick_sort.sort()
print('Quicksort time taken: %s' % str(time.time() - t))

radix_sort = radix(n)

random.shuffle(n)

t = time.time()
radix_sort.sort()
print('Radix sort time taken: %s' % str(time.time() - t))

# Quicksort time taken: 0.12093067169189453
# Radix sort time taken: 0.04897117614746094
