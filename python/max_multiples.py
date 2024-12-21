def max_multiple(divisor, bound):
    #your code here
    if bound % divisor == 0 and bound > 0:
        return bound
    else:
        return max_multiple(divisor, bound - 1)

def max_multiple_optimized_one(divisor, bound):
    return bound - (bound % divisor)

def max_multiple_optimized_two(divisor, bound):
    return bound // divisor * divisor
