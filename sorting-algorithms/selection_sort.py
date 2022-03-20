
def selection_sort(nums):

    # (N-1) * N == O(N^2)
    for i in range(len(nums)-1):
        index = i
        print("I : ", nums[i])
        # Linear search O(N)
        for j in range(i, len(nums)):
            print("J : ", nums[j])
            print("I, J : ", i, " , ", j)
            if nums[j] < nums[index]:
                index = j

        if index != i:
            nums[index], nums[i] = nums[i], nums[index]


n = [97, -10, 7, 56, -14, 3, 12]
print(n)
selection_sort(n)
print(n)
# Fast only when size of Array is less than 10
