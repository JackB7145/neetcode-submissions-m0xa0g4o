class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        from functools import cmp_to_key

        copy = words.copy()
        # build rank map
        rank = {ch: i for i, ch in enumerate(order)}

        def alien_compare(a, b):
            n = min(len(a), len(b))
            for i in range(n):
                if a[i] != b[i]:
                    return rank[a[i]] - rank[b[i]]
            # prefix case
            return len(a) - len(b)

        words.sort(key=cmp_to_key(alien_compare))

        return copy == words