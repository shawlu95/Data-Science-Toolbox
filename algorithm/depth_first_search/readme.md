### Basic Structure

```Python
def dfs(graph, r, c, **kargs):
    # base case
    if base_case:
        return

    # make change
    saved = raph[r][c]
    graph[r][c] = "."

    # recurse
    res = any(dfs(args) for i in [...])

    # undo change
    graph[r][c] = saved

    # backtrack
    return res
```

### Primer
* Find contiguous block in matrix [[200](200_Number_of_Islands.py)].
* Find combination that sums up to target [[39](39_Combination_Sum.py)].
* Find combination (with duplicate elements) that sums up to target [[40](39_Combination_Sum_II.py)].
