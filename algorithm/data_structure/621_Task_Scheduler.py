import heapq
class Solution(object):
    # using heap n log(26)
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        n += 1
        ans = 0
        d = collections.Counter(tasks)
        heap = [-c for c in d.values()]
        heapq.heapify(heap)
        while heap:
            stack = []
            cnt = 0
            for _ in range(n):
                if heap:
                    c = heapq.heappop(heap)
                    cnt += 1
                    if c < -1:
                        stack.append(c + 1)
            for item in stack:
                heapq.heappush(heap, item)
            ans += n if heap else cnt # == if heap then n else cnt
        return ans

    def leastInterval2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord("A")] += 1
        count.sort()
        time = 0
        while count[-1] > 0:
            print(count)
            i = 0
            while i <= n:
                if count[-1] == 0:
                    # all tasks processed, return
                    break
                # keep trying to do less urgent tasks
                # if no such task needs to be done, if clause is not executed
                if i < 26 and count[25 - i] > 0:
                    count[25 - i] -= 1
                time += 1
                i += 1
            # only resort after cooling time
            count.sort()
        return time