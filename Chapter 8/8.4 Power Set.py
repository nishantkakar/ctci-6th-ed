def power_set(arr):
    """
    :type arr: list
    :rtype: list
    """
    subsets = [[]]
    for i in arr:
        for j in range(len(subsets)):
            subsets.append(subsets[j] + [i])
    return subsets

x = [1, 2, 3]
print power_set(x)
