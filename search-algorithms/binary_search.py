
def binary_search(data, item, left, right):
    if right < left:
        print("Item not found")
        return -1
    middle = (left + right) // 2
    if data[middle] == item:
        print("Found element : ", data[middle], " at position ", middle)
        return middle
    elif item < data[middle]:
        return binary_search(data, item, left, middle-1)
    elif item > data[middle]:
        return binary_search(data, item, middle+1, right)


nums = [-13, -2, 3, 5, 17, 58, 97, 103]
binary_search(nums, -130, 0, len(nums)-1)
