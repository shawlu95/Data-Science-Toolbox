class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i, j = 0, len(S)
        ans = []
        while i != j:
            for c in S:
                if c == "I":
                    ans.append(i)
                    i += 1
                else:
                    ans.append(j)
                    j -= 1
        ans.append(i)
        return ans