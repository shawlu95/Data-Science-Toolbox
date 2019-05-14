"""
[LintCode] 183 Wood Cut
Description
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

Notice
You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.


Example
For L=[232, 124, 456], k=7, return 114.


Challenge
O(n log Len), where Len is the longest length of the wood.
"""

def woodCut(arr, k):
    """
    arr: array of integer denoting lengths of wood
    k: required number of uniform cut

    Note that not every element needs to be cut.
    If k = 1, simply return the largest.

            lr
    OOOOO...OOXX...XXX
             lr
    Complexity O(N + LogM), N = len(arr), M = max(arr)
    """

    l, r = 0, max(arr)
    count = lambda arr, x: sum(a // x for a in arr)
    while l + 1 < r:
        m = (r - l) // 2 + l
        if count(arr, m) == k:
            l = m
        elif count(arr, m) < k:
            # cut size too big
            r = m - 1
        else:
            # cut size too small
            # cannot add, or l may point to X
            l = m
    if count(arr, r) == k:
        return r
    elif count(arr, l) == k:
        return l
    return 0

print(woodCut([232, 124, 456], k=7)) # 114
