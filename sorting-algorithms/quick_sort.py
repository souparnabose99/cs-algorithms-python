
# O(NLogN) runtime complexity -> O(N^2) for worst case
class QuickSort:

    def __init__(self, data):
        self.data = data

    def sort(self):
        self.quick_sort(0, len(self.data)-1)

    # Low is index of first item, high is index of last item
    def quick_sort(self, low, high):
        if low >= high:
            return
        pivot_index = self.partition(low, high)
        # Do recursive call on left and right sub-array
        self.quick_sort(low, pivot_index - 1)
        self.quick_sort(pivot_index + 1, high)

    def partition(self, low, high):
        pivot = (low + high) // 2
        self.data[pivot], self.data[high] = self.data[high], self.data[pivot]
        # Consider all the other items and compare them with the pivot
        for j in range(low, high):
            if self.data[j] <= self.data[high]:
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low += 1

        # After all item consideration, swap pivot with low
        self.data[low], self.data[high] = self.data[high], self.data[low]

        return low


if __name__ == "__main__":
    data = [1, -4, 0, 15, 3, 97, 19, 54, 23]
    print(data)
    qs = QuickSort(data)
    qs.sort()
    print("Sorted data : ", data)


