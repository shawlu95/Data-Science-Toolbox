class Solution(object):
    def simplifyPath(self, path):
        # multiple consecutive slashes are replaced by a single one.
        # do it by ignoring ""
        places = [p for p in path.split("/") if p!="." and p!=""]
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)