from collections import deque
def max_in_sliding_window(arr, window_size):
    """
    Given a list of integers, find the maximum number in a sliding window
    of size `window_size` where the window slides from left to right by
    one position each time.

    Args:
        arr: the list the window slides over
        window_size: the size of the window

    Returns:
        a list of numbers representing the max in the window at each step
    """
    if (arr is None or len(arr) == 0 or len(arr) < window_size):
        return []
    if (window_size <= 0):
        raise ValueError("window size must be greater than zero!")

    answer = []
    curr = deque([])
    first_elem_index = 0

    for i in range(0, window_size):
        while(len(curr) != 0 and curr[-1] < arr[i]):
            curr.pop()
        if (len(curr) == 0):
            first_elem_index = i
        curr.append(arr[i])
    answer.append(curr[0])

    i = window_size
    while(i < len(arr)):
        if (first_elem_index + window_size == i):
            curr.popleft()
        while(len(curr) != 0 and curr[-1] < arr[i]):
            curr.pop()
        if (len(curr) == 0):
            first_elem_index = i
        curr.append(arr[i])
        answer.append(curr[0])
        i += 1

    return answer
