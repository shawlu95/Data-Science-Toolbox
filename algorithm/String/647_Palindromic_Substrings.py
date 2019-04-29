class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        #  The middle of the palindrome could be in one of 2N - 1 positions: either at letter or between two letters.
        N = len(s)
        for c in range(2 * N - 1):
            # if c between letter (odd), r - l == 1
            # if c at letter (even), r == l
            l = c // 2
            r = l + c % 2
            while l >= 0 and r < N and s[l] == s[r]: 
                # already accounted single letter
                ans += 1
                l -= 1
                r += 1
        return ans
            