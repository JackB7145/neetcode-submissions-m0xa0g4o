class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict

        need = Counter(t)
        window = defaultdict(int)

        def valid():
            for c in need:
                if window[c] < need[c]:
                    return False
            return True

        l = 0
        res_len = float("inf")
        res = ""

        for r in range(len(s)):
            window[s[r]] += 1

            # shrink while valid
            while valid():
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = s[l:r + 1]

                window[s[l]] -= 1
                l += 1

        return res