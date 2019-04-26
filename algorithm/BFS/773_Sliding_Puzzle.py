import itertools

class Solution(object):
    def slidingPuzzle(self, board):
        R, C = len(board), len(board[0])

        # flatten to 1-D turple, note that list is not hashable
        start = tuple(itertools.chain(*board))

        # get index of element 0 from turple
        queue = [(start, start.index(0), 0)]

        seen = {start}
        target = tuple(list(range(1, R * C)) + [0])

        while queue:
            board, posn, depth = queue.pop(0)
            if board == target:
                return depth
            for d in (-1, 1, -C, C):
                nei = posn + d

                # only row or col can differ by 1, but not both
                if abs(nei//C - posn//C) + abs(nei%C - posn%C) != 1:
                    print(board, nei, posn)
                    print(nei//C, posn//C)
                    print(nei%C, posn%C)
                    continue

                if 0 <= nei < R * C:
                    newboard = list(board)
                    newboard[posn], newboard[nei] = newboard[nei], newboard[posn]
                    newt = tuple(newboard)
                    if newt not in seen:
                        print(newt)
                        seen.add(newt)
                        # position of 0 is now at nei
                        queue.append((newt, nei, depth + 1))
        print(board)
        print(target)
        return -1
solver = Solution()
solver.slidingPuzzle([[1,2,3],[4,0,5]])