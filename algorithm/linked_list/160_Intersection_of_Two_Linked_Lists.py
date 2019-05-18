# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        nodesA = set()
        nodeA = headA
        while nodeA:
            nodesA.add(nodeA)
            nodeA = nodeA.next

        nodeB = headB
        while nodeB:
            if nodeB in nodesA:
                return nodeB
            nodeB = nodeB.next
        return None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# if( null==headA || null==headB )
#       return null;

#     ListNode curA = headA, curB = headB;
#     while( curA!=curB){
#       curA = curA==null?headB:curA.next;
#       curB = curB==null?headA:curB.next;
#     }
#     return curA;

class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:

            # when reaching last element, it has no next
            # if nodeA.next:
            #     nodeA = nodeA.next
            # else:
            #     nodeA = headB
            print(nodeA.val, nodeB.val)
            if nodeA:
                nodeA = nodeA.next
            else:
                nodeA = headB

            if nodeB:
                nodeB = nodeB.next
            else:
                nodeB = headA

        return nodeB

