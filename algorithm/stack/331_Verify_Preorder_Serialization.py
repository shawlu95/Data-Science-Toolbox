class Solution:
    """
    A node must have two children: missing one is marked as #.
    "#" does not have children.
         _9_
        /   \
       3     2
      / \   / \
     4   1  #  6
    / \ / \   / \
    # # # #   # #

    Serialization: [9,3,4,#,#,1,#,#,2,#,6,#,#]
    """
    def isValidSerialization(self, preorder: str) -> bool:
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for c in preorder.split(','):
            stack.append(c)
            # while stack[-2:] == ['#', '#']:

            # must use >=, because stack = [#, #] should return False
            # case: [1,#,#,#,#]
            while len(stack) >= 2 and stack[-2] == stack[-1] == u'#':
                stack.pop()
                stack.pop()
                if not stack:
                    return False

                # once a node is checked, it's marked "#" in stack.
                # It's children are removed from stack
                stack[-1] = u'#'
                # breakpoint
            print(stack)
        return stack == [u'#']

"""
Trace
stack = [9]
stack = [9, 3]
stack = [9, 3, 4]
stack = [9, 3, 4, #]

         _9_
        /   \
       3     2
      / \   / \
     #   1  #  6
        / \   / \
        # #   # #
stack = [9, 3, 4, #, #] -> [9, 3, #]
stack = [9, 3, #, 1]
stack = [9, 3, #, 1, #]

         _9_
        /   \
       3     2
      / \   / \
     #   #  #  6
              / \
              # #

         _9_
        /   \
       #     2
            / \
            #  6
              / \
              # #
stack = [9, 3, #, 1, #, #] -> [9, 3, #, #] -> [9, #]
stack = [9, #, 2]
stack = [9, #, 2, #]
stack = [9, #, 2, #, 6]
stack = [9, #, 2, #, 6, #]

         _9_
        /   \
       #     2
            / \
            #  #

         _9_
        /   \
       #     #

stack = [9, #, 2, #, 6, #, #] -> [9, #, 2, #, #] -> [9, #, #] -> [#]
return True
"""
