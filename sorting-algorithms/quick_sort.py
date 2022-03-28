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
