def findFirst(arr, a):
  """
  Unlike binary search, cannot return in the loop. The
  purpose of while loop is to narrow down the search range.

  Can combine two conditions: `arr[m] >= a`
  """
  if not arr: return -1
  l, r = 0, len(arr) - 1

  # exit loop when l + 1 == r, i.e. consecutive
  while l + 1 < r:
    # avoid integer overflow
    m = (r - l) // 2 + l

    if arr[m] == a:
      # cannot do r = m - 1, because
      # m could be the first occurrence
      # out-of-bound error also possible
      r = m
    elif arr[m] > a:
      # can do r = m - 1
      r = m
    else:
      # can do l = m + 1
      l = m

  # three possible result: XXOO
  if arr[l] == a:
    # XXOO
    #   ^^
    return l
  elif arr[r] == a:
    # XXOO
    #  ^^
    return r
  # XXYY, X < O < Y
  #  ^^
  return -1 # not found
