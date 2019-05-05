### Basic Structure
* Initialize `r` to `len(arr) - 1`, not `len(arr)`, which causes index out of bound error.
* `l = m + 1`: need to increment by 1 because integer division rounds down. Think of the case where `r` points to `a` and `l` is repeated moving right.
* `r = m - 1`: `r = m` may get stuck if `a` is not found and `l` can not move right. Then need to move `r` repeatedly left until l - r == 1.
* If `a` is not found, `l` is where `a` should have been inserted in the sorted array. (l - r = 1)

```Python
def bsearch(arr, a):
  l, r = 0, len(arr) - 1
  while l <= r:
    m = (l + r) // 2
    if arr[m] == a:
      return m
    elif arr[m] < a:
      # search right
      l = m + 1
    else:
      # arr[m] > a, search left
      r = m - 1
  return -1 # not found
```

### Primer
* Plain vanilla binary search while loop [[704](704_Binary_Search.py)]
* Plain vanilla binary search recursion [[457](457_Classical_Binary_Search.py)]
* Plain vanilla binary search for insert position [[35](35_Search_Insert_Position.py)]

### Application
* Find point of change (first occurrence of a new series) [[278](278_First_Bad_Version.py)]
