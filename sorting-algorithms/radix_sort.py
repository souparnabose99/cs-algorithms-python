

ITEMS_IN_BUCKET = 10


class RadixSort:

    def __init__(self, data):
        self.data = data

    def get_digits(self):
        return len(str(max(self.data)))

    def sort(self):
        for digit in range(self.get_digits()):
            self.counting_sort(digit)

    def counting_sort(self, d):
        count_array = [[] for _ in range(ITEMS_IN_BUCKET)]
        # store the count of each element in count array with O(N) runtime complexity
        for num in self.data:
            # calculate the index of the given bucket
            index = (num // (10 ** d)) % 10
            count_array[index].append(num)

        # consider all the items in the count array list
        z = 0
        for i in range(len(count_array)):
            while len(count_array[i]) > 0:
                self.data[z] = count_array[i].pop(0)
                z += 1


if __name__ == "__main__":

    n = [5, 2, 132, 114, 21, 60, 89]
    print(n)
    radix_sort = RadixSort(n)
    radix_sort.sort()
    print(n)
