# Binary search algorithm
def binary_search(arr, x):
    """Standard python binary search algorithm implementation.

    Args:
        arr (array[float]): Array to search.
        x (float): Value to search for.

    Returns:
        An integer corresponding to the index to target value is found in.
        Returns -1 if target value is not in array.
    """

    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
     
    return -1