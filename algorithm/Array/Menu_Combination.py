menu = [2.15, 2.75, 3.35, 3.6, 4.2, 5.8]
limit = 4.3

# identical to 39. Combination Sum

# 2.15
#    | 2.15 good
#    | 2.75 bad - break
# 2.75
#    | 2.75 bad - break
# 3.35 bad -break

# summary:
# sort elements first
# if target is zero:
#    base case, add combo to ans
# iterate with index 0, 1 ... len(menu) - 1
#     if adding element is less equal target, recurse

def findCombination(menu, limit):
    # a list of list, each list is a valid combination
    ans = []

    menu.sort()

    def dfs(start, path, menu, rem, ans):
        if rem == 0:
            ans.append(path)
            return
        for i in range(start, len(menu)):
            if menu[i] <= rem:
                dfs(i, path + [menu[i]], menu, rem - menu[i], ans)
            else:
                return

    dfs(0, [], menu, limit, ans)
    print(ans)
    return ans


findCombination(menu, limit)