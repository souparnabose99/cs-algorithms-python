
# O(2^N) Exponential runtime complexity
def hanoi_impl(disk, source, middle, destination):

    # Base case: Index 0 implies smallest disc and 2 is largest
    if disk == 0:
        print("Disk %s from %s to %s" % (disk, source, destination))
        return

    # moving n-1 disks
    hanoi_impl(disk - 1, source, destination, middle)
    print("Disk %s from %s to %s" % (disk, source, destination))
    hanoi_impl(disk - 1, middle, source, destination)


hanoi_impl(2, "A", "B", "C")

