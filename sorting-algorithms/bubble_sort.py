import time


class BubbleSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-i-1):
                # for desc order, change > to < and run the algorithm
                if self.nums[j] > self.nums[j+1]:
                    self.swap(j, j+1)
        return self.nums

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


if __name__ == "__main__":
    # O(N^2) runtime complexity
    print("Unsorted : [83, -1, 3, 19, -17, 2]")
    bs = BubbleSort([83, -1, 3, 19, -17, 2])
    start = time.time()
    bs.sort()
    print(bs.nums)
    end = time.time()
    print("Run time : ", end - start)

# Unsorted : [83, -1, 3, 19, -17, 2]
# [-17, -1, 2, 3, 19, 83]
# Run time :  0.0
