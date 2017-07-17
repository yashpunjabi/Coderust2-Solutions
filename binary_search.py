def binary_search(arr, item):
    """
    Find `item` in the sorted list `arr` using binary search.

    Args:
        arr: the list to search in
        item: the item to search for in `arr`

    Returns:
        the index of the `item` in `arr` or -1 if not found
    """
    if (len(arr) <= 0):
        return -1

    start = 0
    end = len(arr) - 1
    return _binary_search(arr, item, start, end)

def _binary_search(arr, item, start, end):
    if (start > end):
        return -1
    middle = (start + end) // 2
    if (arr[middle] == item):
        return middle
    elif (arr[middle] < item):
        start = middle + 1
        return _binary_search(arr, item, start, end)
    else:
        end = middle - 1
        return _binary_search(arr, item, start, end)
