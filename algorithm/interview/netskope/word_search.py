inBound = lambda r, c: r < len(board) and c < len(board[0])

def dfs(board, r, c, word):
    # base case (r, c can be out of bound here)
    if word == "": return True
    if not inBound(r, c): return False

    # check for out-of-bound after base case
    return any(dfs(board, r + dr, c + dc, word[1:])
              for dr, dc in [(1, 0), (0, 1), (1, 1)]
              if word[0] == board[r][c])

def exist(board, word):
    return any(dfs(board, r, c, word)
               for r in range(len(board))
               for c in range(len(board[0])))

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

assert(exist(board, "ESE") == True)
assert(exist(board, "ASA") == True)
assert(exist(board, "ABCE") == True)
assert(exist(board, "ADEE") == True)
assert(exist(board, "BFCE") == True)
assert(exist(board, "ECCE") == False)
assert(exist(board, "ADFC") == False)
assert(exist(board, "") == True)
assert(exist([], "BFCE") == False)
assert(exist([[]], "BFCE") == False)
