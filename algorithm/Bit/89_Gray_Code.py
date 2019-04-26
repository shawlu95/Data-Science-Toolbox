class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if not n:
            return [0]
        res = [0, 1]
        # start with n = 1, we have 0000 0001
        # n = 2: 0000 0001 0011 0010
        # n = 3: 0000 0001 0011 0010 0110 0111 0101 0100
        # note that we append element in reverse order, each with prefix 1

        # include n
        for i in range(2, n + 1):
            for j in range(len(res) - 1, -1, -1):
                # using OR to add prefix 1
                res.append(res[j] | 1 << i - 1)
        return res