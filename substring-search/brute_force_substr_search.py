
def naive_search(pattern, text):
    n = len(text)
    m = len(pattern)
    # Do single character matching from left to right, shift by 1 if there is a mismatch

    # O(N)
    for i in range(n-m+1):
        j = 0
        # Worst case : O(N*M)
        while j < m:
            if text[i+j] != pattern[j]:
                break

            j += 1
        if j == m:
            print("Found matching pattern at index : ", i)


naive_search("abc", "dhe ua bibabc")
