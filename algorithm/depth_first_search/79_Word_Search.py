class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        def dfs(board, r, c, word):
            if word == "":
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            val = board[r][c]
            if val == word[0]:

                board[r][c] = "$"

                res = False
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # if 0 <= r + dr < len(board) and 0 <= c + dc < len(board[0]):
                    res |= dfs(board, r + dr, c + dc, word[1:])

                # note: put back the character to be reused by other path
                board[r][c] = val

                return res
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                # note: do not return false if one candidate is false
                if dfs(board, r, c, word):
                    return True
        return False

    def exist2(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
              or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        board[i][j] = tmp
        return res

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCB"

solver = Solution()
print(solver.exist([["a"]], "a"))