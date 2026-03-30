from collections import deque

class TrieNode:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.tree = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.tree
        for c in word:
            if c not in curr.next:
                curr.next[c] = TrieNode()
            curr = curr.next[c]
        curr.isEnd = True

    def jump(self, jumps, starts):
        queue = deque(starts)
        while jumps > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                for nxt in node.next.values():
                    queue.append(nxt)
            jumps -= 1
        return list(queue)

    def search(self, word: str) -> bool:
        nodes = [self.tree]
        dots = 0

        for c in word:
            if c == '.':
                dots += 1
                continue

            if dots > 0:
                nodes = self.jump(dots, nodes)
                dots = 0

            next_nodes = []
            for node in nodes:
                if c in node.next:
                    next_nodes.append(node.next[c])

            if not next_nodes:
                return False

            nodes = next_nodes

        if dots > 0:
            nodes = self.jump(dots, nodes)

        return any(node.isEnd for node in nodes)
