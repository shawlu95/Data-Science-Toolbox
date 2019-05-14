# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        九章算法模版(LeetCode accepted).
        Note that end index is inclusive (version n).
        """
        l, r = 0, n
        while l + 1 < r: # cannot have equal sign, because r = m may get stuck
            m = (r - l) // 2 + l
            if isBadVersion(m):
                # cannot do r <- m - 1, because m can be first bad
                # out-of-bound error also possible
                r = m
            else:
                # m is a good version, first bad version must be > m
                l = m + 1

        # three possible results
        if isBadVersion(l):
            # OOXX
            #   ^^

            # XXXX
            # ^^
            return l
        elif isBadVersion(r):
            # OOXX
            #  ^^
            return r

        # OOOO
        #   ^^
        return -1 # no bad version

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l < r: # cannot have equal sign, because r = m may get stuck
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l

# plain bsearch
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        each middle point can be GG, GB or BB
        GG: l <- m + 1
        GB: return m
        BB: r <- m - 1
        """
        l, r = 1, n
        while l <= r:

            m = (l + r) // 2
            if not isBadVersion(m) and isBadVersion(m + 1):
                # return first bad version, not last good version
                return m + 1
            elif not isBadVersion(m) and not isBadVersion(m + 1):
                # two good, search right
                l = m + 1
            elif isBadVersion(m) and isBadVersion(m + 1):
                # two bad, search left
                r = m - 1

        # edge case:
        # first version bad: 10, 1
        # last version bad: 10, 10
        return l
