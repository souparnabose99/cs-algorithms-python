
def merge_sort(nums):
    # Keep splitting list into sub lists until sub lists have 1 item and array with single value is sorted by default
    if len(nums) == 1:
        return

    # Divide phase
    middle_index = len(nums) // 2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    # Conquer phase
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1

        k += 1
    # There might be additional operations in the left or right sub array
    while i < len(left_half):
        nums[k] = left_half[i]
        i += 1
        j += 1

    while j < len(right_half):
        nums[k] = right_half[j]
        j += 1
        k += 1


n = [97, 0, -10, 5, 16, -3, 100]
print(n)
merge_sort(n)
print(n)

# [97, 0, -10, 5, 16, -3, 100]
# [-10, -3, 0, 5, 16, 97, 100]





