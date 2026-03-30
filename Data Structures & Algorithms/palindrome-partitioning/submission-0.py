class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_pal(l, r):
            # manual palindrome check, character by character
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(idx, temp):
            if idx == len(s):
                res.append(temp[:])
                return

            for i in range(idx, len(s)):
                # check substring s[idx:i+1]
                if is_pal(idx, i):
                    temp.append(s[idx:i+1])
                    backtrack(i + 1, temp)
                    temp.pop()

        backtrack(0, [])
        return res
