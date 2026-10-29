class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + letter + word[i+1:]

                    if newWord in words:
                        queue.append((newWord, steps + 1))
                        words.remove(newWord)

        return 0