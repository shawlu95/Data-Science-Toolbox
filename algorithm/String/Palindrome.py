# def palindrome(s):
#     # Write your code here
#     ans = set()
#
#     l = 1
#
#
#     while l <= len(s):
#         for i in range(len(s) - l + 1):
#             sub = s[i:i + l]
#
#             if sub == sub[::-1] and sub not in ans:
#                 print(sub)
#                 ans.add(sub)
#         l += 1
#     return len(ans)
#
# print(palindrome("aabaa"))

def longestChain(words):
    # Write your code here
    wordSet = set(words)
    ans = []
    def dfs(wordSet, word, c, ans):
        if len(word) == 1:
            print(c)
            ans.append(c)
            return
        for i in range(len(word)):
            candS = word[:i] + word[i + 1:]
            print(candS)
            if candS in wordSet:
                dfs(wordSet, candS, c + 1, ans)
    for word in words:
        dfs(wordSet, word, 1, ans)
    print(ans)
    return ans

longestChain(["a",
             "b",
             "ba",
             "bca",
             "bda",
             "bdca"])