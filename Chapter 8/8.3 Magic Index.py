# using an iterative approach
def magic_index(arr):
    """
    :param arr: integer list
    :type arr: list
    :return: magic index of the list
    :rtype: int
    """
    start = 0
    end = len(arr)
    mid = (start + end) / 2
    while start <= end:
        if arr[mid] == mid:
            return mid
        elif mid > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) / 2
    return -1


a = [-3, -1, 0, 1, 3, 5, 7, 9]
print magic_index(a)
