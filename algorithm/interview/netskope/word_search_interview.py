def dfs(board, r, c, word):
    # base case (r, c can be out of bound here)
    if word == "":
        return True

    # bug: check inBound here, not in any()
    inBound = lambda r, c: 0 <= r < len(board) and 0 <= c < len(board[0])

    # check for out-of-bound after base case
    return any(dfs(board, r + dr, c + dc, word[1:])
              for dr, dc in [(1, 0), (0, 1), (1, 1)]
              if inBound(r + dr, c + dc)
              and word[0] == board[r][c])

def exist(board, word):
    if not word:
        return True

    nrows = len(board)
    if nrows == 0:
        return False

    ncol = len(board[0])
    if ncols == 0:
        return False

    return any(dfs(board, r, c, word)
               for r in range(len(board))
               for c in range(len(board[0])))
