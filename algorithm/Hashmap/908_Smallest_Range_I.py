class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        # if max(A) - K < min(A) + K, do not have to move full range K
        return max(max(A) - K - (min(A) + K), 0)