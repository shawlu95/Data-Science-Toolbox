class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == " ":
            return ""

        s = list(s[::-1])
        print(len(s))
        l, r = 0, 0
        while r < len(s) + 1:
            # the two condition must not be reversed, or the second condiiton will throw exception
            if  r == len(s) or s[r] == " ":
                e = r - 1
                while l < e:
                    s[l], s[e] = s[e], s[l]
                    l += 1
                    e -= 1
                l = r + 1
            r += 1
        return "".join(s)

    def reverseWords2(self, s):
        new_string = ""
        j = len(s)
        # iterate the str in a reversed order
        for i in range(len(s)-1,-1,-1):
            # trim the trailing space
            if s[i] == " ":
                j = i
            # if we encountered a " " before the worlds, we know a word ended here, append " " or the word
            elif i == 0 or s[i-1] == " ":
                if len(new_string) != 0:
                    new_string += " "
                new_string += s[i:j]
        return new_string

solver = Solution()
print(solver.reverseWords2("the sky is blue"))