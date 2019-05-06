# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# tortoise hare solution
class Solution(object):
    def detectCycle(self, head):
        def getIntersection(head):
            s = head
            f = head

            # phase 1
            # if use while s.val != f.val, the loop is never entered
            while f and f.next:
                s = s.next
                f = f.next.next

                if s == f:
                    return s

            # no intersection
            return

        intersection = getIntersection(head)
        if not intersection:
            return

        print("intersection", intersection.val)

        # phase 2
        ptr1, ptr2 = head, intersection
        while ptr1 != ptr2:
            ptr1, ptr2 = ptr1.next, ptr2.next

        return ptr1


# hash table solution
class Solution(object):
    # clean version (solution)
    def detectCycle(self, head):
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None

    # unclear output spec, same logic
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = {}

        cur = head
        i = 0
        while cur and cur.val not in visited:
            visited[cur.val] = i
            cur = cur.next
            i += 1

        if not cur:
            return None
        return "tail connects to node index %i" % visited[cur.val]

    def detectCycle2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = {}

        # dummy = ListNode()
        # dummy.next = head

        cur = head
        i = 0
        while cur:
            if cur.val in visited:
                return "tail connects to node index %i" % visited[cur.val]
            visited[cur.val] = i
            cur = cur.next
            i += 1

        return "no cycle"

dummy = cur = ListNode(None)
vals = [3,2,0,-4]
cycle = 1

vals = [1,2]
cycle = 0

vals = [1]
cycle = -1

start = None
for i, val in enumerate(vals):
    next = ListNode(val)
    cur.next = next
    cur = cur.next
    if i == cycle:
        start = cur

cur.next = start

head = dummy.next

solver = Solution()
print(solver.detectCycle(head))