class Solution:
    def isValid(self, s: 'str') -> 'bool':
        if not s:
            return True
        stack = []
        bracket = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        # corner case: "]", stack is empty when in first iteration
        for c in s:
            if c in bracket:
                # open a bracket
                stack.append(c)
            else:
                # try closing a bracket
                if not stack or bracket[stack.pop()] != c:
                    return False

        # corner case "(", stack is non-empty upon end of function
        return len(stack) == 0
