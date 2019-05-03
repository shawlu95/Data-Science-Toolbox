class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if c == "]":
                stack.pop() # remove closing bracket
                
                # retrieve string to repeat
                strBuffer = ""
                while stack[-1] != "[":
                    # careful, insert new char to front
                    strBuffer = stack.pop() + strBuffer
                
                stack.pop() # remove opening bracket
                
                # retrieve multiplier; careful, stack may be empty
                mult = ""
                while stack and stack[-1].isdigit():
                    # careful, insert new char to front
                    mult = stack.pop() + mult
                
                # messed up order when element gets reused in nested brackets
                # stack.append(strBuffer[::-1] * int(mult[::-1]))
                stack.append(strBuffer * int(mult))
                # print(mult, strBuffer, stack)
        
        return "".join(stack)
            