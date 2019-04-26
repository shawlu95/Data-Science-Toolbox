class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.isWord = True

    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.isWord

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True


class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root

        # since we have n words, root of prefix tree can have up to n branches
        for w in words:
            trie.insert(w)
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.dfs(board, node, r, c, "", res)
        return res

    def dfs(self, board, node, r, c, path, res):
        if not node:
            return
            # reaching end of a prefix tree
        # mark it as false so it won't be duplicated
        if node.isWord:
            res.append(path)
            node.isWord = False

        # out of bound check
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return

        tmp = board[r][c]
        board[r][c] = "#"
        node = node.children.get(tmp)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            candr, candc = r + dr, c + dc
            self.dfs(board, node, candr, candc, path + tmp, res)
        board[r][c] = tmp