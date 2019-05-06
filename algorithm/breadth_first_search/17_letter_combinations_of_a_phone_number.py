class Solution(object):
    def letterCombinationsHelper(self, A, c, s, S):
        if c == len(A):
            S.append(s)
            return
        for i in range(len(A[c])):
            s_ = s + A[c][i]
            self.letterCombinationsHelper(A, c + 1, s_, S)
        return S

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        map = {
            "2" : list("abc"),
            "3" : list("def"),
            "4" : list("ghi"),
            "5" : list("jkl"),
            "6" : list("mno"),
            "7" : list("pqrs"),
            "8" : list("tuv"),
            "9" : list("wxyz")
        }
        A = [map[n] for n in list(digits)]
        return self.letterCombinationsHelper(A, c = 0, s = "", S = [])

solver = Solution()

ans = solver.letterCombinations("29")