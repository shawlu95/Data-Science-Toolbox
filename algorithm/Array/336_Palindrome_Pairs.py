class Solution:
    # O (n m m)
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        # O(m), m is word length
        def is_palindrome(check):
            return check == check[::-1]


        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)

            # n is a valid slicing index
            for j in range(n + 1):
                pref = word[:j]
                suf = word[j:]

                # set front != word to avoid appending word / prepending word to itself
                if is_palindrome(pref):
                    front = suf[::-1]
                    if front != word and front in words:
                        valid_pals.append([words[front], k])

                # avoid duplicate, when j == n, suf is empty string
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals