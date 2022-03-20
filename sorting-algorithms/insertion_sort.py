
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        # Check for previous items
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j = j - 1


n = [97, -10, 7, 56, -14, 3, 12]
print(n)
insertion_sort(n)
print(n)
# Works faster than quick/merge sort when no of items less than 20
