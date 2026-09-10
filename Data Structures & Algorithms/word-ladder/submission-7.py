class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = set()

        mask_to_word = defaultdict(list)

        for word in wordList:
            for idx in range(len(word)):
                mask_to_word[word[:idx]+'*'+word[idx+1:]].append(word)


        queue = deque([(beginWord, 1)])

        while queue:
            word, cnt = queue.popleft()
            if word == endWord:
                return cnt

            seen.add(word)

            for idx in range(len(word)):
                newMask = word[:idx]+'*'+word[idx+1:]
                for string in mask_to_word[newMask]:
                    if string not in seen:
                        queue.append((string, cnt+1))
            
        return 0