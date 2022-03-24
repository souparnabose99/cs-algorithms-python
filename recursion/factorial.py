
def factorial_head(n):
    if n == 0:
        return 1
    sub_result_1 = factorial_head(n-1)
    result = n*sub_result_1
    # We return to previous stack frame every time until stack is empty
    # Last stack frame on the stack memory is the result of the factorial function      
    return result


num = factorial_head(5)
print(num)
