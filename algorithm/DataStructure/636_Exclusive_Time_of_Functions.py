class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        res = [0] * n
        s = logs[0].split(":")
        stack.append(int(s[0]))

        i = 1
        prev = int(s[2])

        while i < len(logs):
            s = logs[i].split(":")
            if s[1] == "start":
                if stack:
                    # if an earlier function has been running, increment its time
                    res[stack[-1]] += int(s[2]) - prev
                stack.append(int(s[0]))
                prev = int(s[2])
            else:
                # if a process just ended, increment its time and pop it
                res[stack[-1]] += int(s[2]) - prev + 1
                stack.pop()
                prev = int(s[2]) + 1
            i += 1
        return res