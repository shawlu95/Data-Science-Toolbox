### Basic Structure

```Python
def dfs(graph, r, c, **kargs):
    """
    Starting at position [r, c], perform DFS
    on a 2D matrix.
    """
    # base case
    if base_case:
        return ...

    # make change
    saved = graph[r][c]
    graph[r][c] = "."

    # take further steps if certain conditions are met
    res = any(dfs(args) for i in [...] if ...)

    # undo change
    graph[r][c] = saved

    # backtrack
    return res
```

### Primer
* Find contiguous block in matrix [[200](200_Number_of_Islands.py)].
* Find combination that sums up to target [[39](39_Combination_Sum.py)].
* Find combination (with duplicate elements) that sums up to target [[40](39_Combination_Sum_II.py)].
* Word search. DFS with list comprehension [[79](79_Word_Search.py)].
