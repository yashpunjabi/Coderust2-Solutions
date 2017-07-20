def quora_upvotes(arr, window_size):
    """
    Solves the question found here: https://www.quora.com/challenges#upvotes
    The solution is found by keeping track of the ranges where non increasing
    or non decreasing subranges can be found.

    Since each subrange has k(k-1)/2 subranges within in (including itself),
    the number of subranges for a window can be found using this list.

    The number of non decreasing subranges is subtracted from the number of non
    increasing subranges to find the answer at each window.

    Args:
        arr: the list to iterate over
        window_size: the size of the window that iterates over the list

    Returns:
        a list as described by https://www.quora.com/challenges#upvotes
    """
    ret = []
    index = 1

    #lists to store the ranges at which non decreasing subsets can be found
    nonDec = []
    nonInc = []

    nonDecStart = 0
    nonDecEnd = 1

    nonIncStart = 0
    nonIncEnd = 1

    while(index < window_size):
        if (arr[index] >= arr[index-1]):
            nonDecEnd += 1
        else:
            nonDec.append((nonDecStart, nonDecEnd))
            nonDecStart = index
            nonDecEnd = index + 1

        if (arr[index] <= arr[index-1]):
            nonIncEnd += 1
        else:
            nonInc.append((nonIncStart, nonIncEnd))
            nonIncStart = index
            nonIncEnd = index + 1

        index += 1
    nonDec.append((nonDecStart, nonDecEnd))
    nonInc.append((nonIncStart, nonIncEnd))

    ret.append(countRanges(nonDec) - countRanges(nonInc))

    while(index < len(arr)):
        firstPair = nonDec[0]
        if (firstPair[1] - firstPair[0] == 1):
            nonDec.pop(0)
        else:
            nonDec[0] = (firstPair[0] + 1, firstPair[1])

        if (arr[index] >= arr[index-1]):
            nonDec[-1] = (nonDec[-1][0], nonDec[-1][1] + 1)
        else:
            nonDec.append((index, index + 1))

        firstPair = nonInc[0]
        if (firstPair[1] - firstPair[0] == 1):
            nonInc.pop(0)
        else:
            nonInc[0] = (firstPair[0] + 1, firstPair[1])

        if (arr[index] <= arr[index-1]):
            nonInc[-1] = (nonInc[-1][0], nonInc[-1][1] + 1)
        else:
            nonInc.append((index, index + 1))

        ret.append(countRanges(nonDec) - countRanges(nonInc))
        index += 1

    return ret

def countRanges(arr):
    total = 0
    for pair in arr:
        k = pair[1] - pair[0]
        total += k * (k - 1) / 2
    return total
