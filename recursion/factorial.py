
# Stack frames are heavily dependent on each other
def factorial_head(n):
    if n == 0:
        return 1
    sub_result_1 = factorial_head(n-1)
    result = n*sub_result_1
    # We return to previous stack frame every time until stack is empty
    # Last stack frame on the stack memory is the result of the factorial function
    return result


# With the help of accumulator, we can eliminate dependency b/w stack frames in stack memory
def factorial_tail(n, accumulator=1):
    if n == 1:
        # We can eliminate below return call by a print statement for tail recursion, but can't do for head
        return accumulator
    # Stack frames are independent of each other
    return factorial_tail(n-1, n * accumulator)


num = factorial_head(5)
print(num)
