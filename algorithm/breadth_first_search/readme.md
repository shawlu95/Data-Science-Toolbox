### Basic Structure
* Edge case: [], [[]]
* Use enumeration to step in four directions.
* Check boundary with lambda function.

```Python
def bfs(grid, r, c):
    nrow = len(grid) # corner case []
    if nrow == 0: return 0
    ncol = len(grid[0]) # corner case [[]]

    # get a lambda function to prevent out-of-bound error
    inBound = lambda r, c: 0 <= r and r < nrow and 0 <= c and c < ncol

    queue = [(r, c)]

    # left, up, right, down
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    grid[r][c] = "0" # mark starter node
    while queue:
        r, c = queue.pop(0) # pop left
        for dr, dc in steps:
            rr, cc = r + dr, c + dc
            if inBound(rr, cc) and grid[rr][cc] == "1":
                grid[rr][cc] = "0" # mark before appending, to avoid revisiting
                queue.append((rr, cc))
```

### Primer
* Plain vanilla BFS, flood fill image [[733](733_Flood_Fill.py)].
* Find contiguous block in matrix [[200](200_Number_of_Islands.py)].

### Classic
* Word Ladder [[127](127_Word_Ladder.py)].
* Word Ladder II [[126](126_Word_Ladder_II.py)].

### Obscure
* Use node to store additional information (depth, search range) [[655](655_Print_Binary_Tree.py)].
