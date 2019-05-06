class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # handle implicit edge case in for loop
        # if not board:
        #     return False

        def dfs(board, r, c, word):
            # base case (r, c can be out of bound here!)
            if word == "":
                return True

            # must check after base case!
            inBound = lambda r, c: 0 <= r < len(board) and 0 <= c < len(board[0])
            if not inBound(r, c):
                return False

            if word[0] == board[r][c]:
                saved = board[r][c]
                board[r][c] = None

                res = any(dfs(board, r + dr, c + dc, word[1:])
                          for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)])

                # note: put back the character to be reused by other path
                board[r][c] = saved
                return res

            return False

        return any(dfs(board, r, c, word)
                   for r in range(len(board))
                   for c in range(len(board[0])))

    # same logic
    def exist2(self, board, word):
        # implicit handling edge case
        # if not board:
        #     return False
        def dfs(board, r, c, word):
            if word == "":  # all the characters are checked
                return True

            inBound = lambda r, c: 0 <= r < len(board) and 0 <= c < len(board[0])
            if not inBound(r, c) or word[0] != board[r][c]:
                return False
            saved = board[r][c]  # first character is found, check the remaining part
            board[r][c] = None  # avoid visit agian

            # check whether can find "word" along one direction
            res = any(dfs(board, r + dr, c + dc, word[1:])
                      for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)])

            board[r][c] = saved
            return res

        return any(dfs(board, r, c, word)
                   for r in range(len(board))
                   for c in range(len(board[0])))

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCB"

solver = Solution()
print(solver.exist([["a"]], "a"))
