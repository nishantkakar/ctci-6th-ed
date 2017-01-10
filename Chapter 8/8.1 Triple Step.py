# Need to solve this memoization
def step_ways(n):
    """
    :type n: int
    :rtype: int
    """
    # Number of ways for 1 step is 1, 2 is 2, and 3 is 4
    arr = [1, 2, 4]
    for i in range(3, n):
        arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])

    return arr[-1]


print "Total Ways: ", step_ways(20)
