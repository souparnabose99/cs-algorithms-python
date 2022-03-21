
# O(N) runtime complexity
# Used when underlying data-structure is unordered
# For ordered ds, use Binary Search with O(logN) or Hash Table with O(1) runtime complexity
def linear_search(data, item):
    for i in range(len(data)):
        if data[i] == item:
            print("Found element : ", data[i], " at position ", i)
            return i
    return -1


def linear_search_recusrsive(data, item, index=0):
    if index > len(data):
        return -1
    if data[index] == item:
        print("Found element : ", data[index], " at position ", index)
        return index
    return linear_search_recusrsive(data, item, index+1)


linear_search([2, 19, 0, 13, 58, 1], 58)
linear_search_recusrsive([2, 19, 0, 13, 58, 1], 1)

# Found element :  58  at position  4
# Found element :  1  at position  5


