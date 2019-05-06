# version 1, use stack
#
# for loop the given string, when encounter non] char, we just add char to stack,
# when char is ], then we look backward, we loop back all alpha chars and put them in a chars list,
# and then pop left bracket char, which should be the next backforward char,
# and then set multi as 0, base as 1, and get the multi, then reverse chars, this is important,
# then append chars string * multi to stack, then return stack as a string
#
# version 2, dfs
#
# recursive version , dfs helper function should return string and index
# in the dfs recursive call, we should loop through chars from the index,
# and if char, append to res list, if num, then get multi, if left, then get dfs call
# and append returned string to res list and returned index is the new index
# if right just return res string and index
# do not forget to index += 1 at the end of while loop

def expand(s):
    i = 1
    l = len(s)
    stack = [s[0]]
    while i < l:
        while i < l and stack[-1] != "]":
            stack.append(s[i])
            i += 1

        # only continue if stack ends with a closing bracket
        # when at string's end, i is out of scope (equal length)
        if i <= l and stack[-1] == "]":
            stack.pop()
            tmp = []
            while stack and stack[-1] != "[":
                tmp.append(stack.pop())
            stack.pop()
            multiplier = int(stack.pop())
            tmp = tmp[::-1]
            for j in range(multiplier):
                for k in range(len(tmp)):
                    stack.append(tmp[k])
        print("".join(stack))

# expand("abc3[a]")
# expand("4[acdy]")
expand("3[2[ad]3[pf]]xyz")