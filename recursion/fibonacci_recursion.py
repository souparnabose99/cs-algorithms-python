
def fibonacci_head(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # 2 recursions, some values are calculated twice -> multiple stack frames with same value
    # Not an efficient recursion
    num_1 = fibonacci_head(n-1)
    num_2 = fibonacci_head(n-2)
    result = num_1 + num_2
    return result


def fibonacci_tail(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b

    return fibonacci_tail(n - 1, b, a + b)


print(fibonacci_head(3))

