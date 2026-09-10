class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        mask_to_word = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                mask = word[:i] + '*' + word[i + 1:]
                mask_to_word[mask].append(word)

        queue = deque([(beginWord, 1)])
        seen = {beginWord}

        while queue:
            word, cnt = queue.popleft()

            if word == endWord:
                return cnt

            for i in range(len(word)):
                mask = word[:i] + '*' + word[i + 1:]

                for neighbor in mask_to_word[mask]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, cnt + 1))

        return 0