class TrieNode:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        idx = 0
        curr = self.root
        while idx < len(word):
            if word[idx] not in curr.children:
                node = TrieNode()
                curr.children[word[idx]] = node
            curr = curr.children[word[idx]]
            idx += 1
        curr.isEnd = True         

    def search(self, word: str) -> bool:
        idx = 0
        curr = self.root
        while idx < len(word):
            if word[idx] not in curr.children:
                return False
            
            curr = curr.children[word[idx]]
            idx += 1

        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        idx = 0
        curr = self.root
        print(prefix, idx, len(prefix), curr.children)
        while idx < len(prefix):
            if prefix[idx] not in curr.children:
                return False
            
            curr = curr.children[prefix[idx]]
            idx += 1

        return True
        
        