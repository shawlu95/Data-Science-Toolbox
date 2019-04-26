class Solution(object):
    # complexity: L * 26 * n
    # L is number of words in wordList
    # n is avg length of word
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = [[beginWord, 1]]
        charSet = {w for word in wordList for w in word}
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                # for c in 'abcdefghijklmnopqrstuvwxyz':
                # for c in string.ascii_lowercase:
                for c in charSet:
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0


class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = [[beginWord, 1]]
        visited = set()
        # breadth first search, good for return length, not specific path
        while queue:
            word, length = queue.pop(0)
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return length

                # permute every letter inside word into every other letter
                # append all valid permutation to queue with incremented length
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i + 1:]
                        if next_word in wordList:
                            # same as marking it as visited
                            # wordList.remove(next_word)

                            if next_word not in visited:
                                queue.append([next_word, length + 1])
        return 0

# bi-directional BFS
class Solution3(object):
    def ladderLength(self, beginWord, endWord, wordList):
        s = beginWord
        e = endWord
        if s == e:
            return 1

        if e not in wordList:
            return 0

        # init two directional queues
        q1, q2 = {s}, {e}  # Note: set not dict

        d = set(wordList)

        steps = 1
        while q1 and q2:
            if len(q1) > len(q2):
                q1, q2 = q2, q1  # balance

            nq = set()
            for x in q1:
                for i in range(len(x)):
                    for t in string.ascii_lowercase:
                        y = x[:i] + t + x[i + 1:]

                        if y in q2:
                            return steps + 1

                        if y in d:
                            d.remove(y)
                            nq.add(y)
            q1 = nq
            steps += 1
        return 0

    # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
