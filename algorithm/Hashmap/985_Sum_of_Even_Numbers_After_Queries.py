class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        running = sum(val for val in A if val % 2 == 0)
        for val, idx in queries:
            pre = A[idx]
            A[idx] += val
            
            # remember to update running!
            if pre % 2 == 0 and val % 2 == 0:
                running = running + val
                ans.append(running) # increment existing
            elif pre % 2 == 1 and val % 2 == 1: 
                running = running + pre + val
                ans.append(running) # add new
            elif pre % 2 == 0 and val % 2 == 1:
                running = running - pre
                ans.append(running) # remove pre
            elif pre % 2 == 1 and val % 2 == 0:
                ans.append(running) # no change in parity
            
        return ans