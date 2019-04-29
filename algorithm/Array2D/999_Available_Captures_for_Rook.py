class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "R":
                    break
            if board[r][c] == "R":
                break
        
        # rook is at position (r, c)
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr, cc = r, c 
            while 0 <= rr and rr < len(board) and 0 <= cc and cc < len(board[0]):
                
                # update in the end, otherwise indices may not be valid
                if board[rr][cc] == "p":
                    print(rr, cc)
                    ans += 1
                    break
                elif board[rr][cc] == "B":
                    break
                
                rr, cc = rr + dr, cc + dc
        return ans
                