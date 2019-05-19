"""
Problem Description:

Given a matrix of letters, and a word. Check whether the word
`exists` in the matrix.

The word can start at any position of the matrix. Every next letter
is connected in three possibe dicrections:
    (1) right
    (2) down
    (3) lower right

Example:
[["C", "B", "A", "N"],
 ["A", "O", "O", "L"],
 ["N", "N", "N", "A"]]

"BON" -> True
"BAN" -> True
"COOL" -> True
"ANNA" -> True
"ANNNA" -> True
"LOOB" -> False
"""

def dfs(board, r, c, word):
    # base case (r, c can be out of bound here)
    if word == "": return True

    if r >= len(board) or c >= len(board[0]): return False

    # check for out-of-bound after base case
    return any(dfs(board, r + dr, c + dc, word[1:])
               for dr, dc in [(1, 0), (0, 1), (1, 1)]
               if word[0] == board[r][c])

def exist(board, word):
    return any(dfs(board, r, c, word)
               for r in range(len(board))
               for c in range(len(board[0])))
