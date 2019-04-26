class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # map each character to its final appearance
        last = {c: i for i, c in enumerate(S)}

        # anchor remembers the start of current partition
        # j moves as far as possible to find the end of current partition
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            # If we are at a label c that occurs last at some index after j,
            # we'll extend the partition j = last[c]
            j = max(j, last[c])

            if i == j:
                # If we are at the end of the partition (i == j)
                # then we'll append a partition size to our answer
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans