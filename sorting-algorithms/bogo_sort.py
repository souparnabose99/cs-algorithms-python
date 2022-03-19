import random
import time


class BogoSort:

    def __init__(self, nums):
        self.nums = nums

    def is_sorted(self):
        for i in range(len(self.nums)-1):
            if self.nums[i] > self.nums[i+1]:
                return False

        return True

    def bogo_sort(self):
        counter = 1
        while not self.is_sorted():
            print("Shuffle the values ...")
            print("No of shuffles : ", counter)
            counter += 1
            self.shuffle()

    # Fisher-Yates shuffle - > Algorithm for generating random permutations of a finite sequence -> O(N)
    def shuffle(self):
        # for i from n−1 down to 1
        for i in range(len(self.nums)-2, -1, -1):
            j = random.randint(0, i+1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


if __name__ == "__main__":
    # O(N!) runtime complexity
    bg = BogoSort([83, -1, 3, 19, -17, 2])
    start = time.time()
    bg.bogo_sort()
    print(bg.nums)
    end = time.time()
    print("Run time : ", end - start)

# No of shuffles :  424
# [-17, -1, 2, 3, 19, 83]
# Run time :  0.04997134208679199

# No of shuffles :  3181
# [-17, -1, 2, 3, 19, 83]
# Run time :  0.21231889724731445

