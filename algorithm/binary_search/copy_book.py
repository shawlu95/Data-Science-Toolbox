def count(arr, x, k):
    """
    If the slowest copier takes x minites to finish his work,
    calcualte how many copiers are needed, which is bounded by k.
    """
    if not arr:
        return 0
    copier = 1
    tmp = arr[0]
    for page in arr[1:]:
        if tmp + page > x:
            copier += 1
            tmp = 0
        tmp += page
    return copier <= k

def copyBook(arr, k):
    """
    arr: list[int] array of books, denoting # pages
    k: int number of people
    Note that cannot divide a book into two persons.
    Assignment of books must be continuous.

    Binary search by the time it takes for the last copier to finish.
    Lower bound is max(arr), someone must copy the largest book.
    Upper bound is sum(arr), one person copies every book.

    Optimum x in [l, .... r]
    When x is large, needs fewer than k copier (O)
    When x is small, needs more than k copier (X)
            lr
    XXX...XXXOOO...OO
             lr
    """
    l, r = max(arr), sum(arr)
    while l + 1 < r:
        m = (r - l) // 2 + l
        if count(arr, m, k):
            # needs to find first position that satisfies
            # cannot decrement m
            r = m
        else: # X
            # each copier needs to do more work
            l = m + 1

    # there are two possible scenarios
    # check left first!
    if count(arr, l, k):
        return l
    return r

print(count([3, 2, 4], x=4, k=2))
print(copyBook([3, 2, 4], k=2))
