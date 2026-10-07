class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(s) and j == len(p):
                return True

            if j >= len(p):
                return False

            # If pattern is something like a*
            if j + 1 < len(p) and p[j + 1] == "*":
                target = p[j]

                # Option 1: use zero occurrences of target
                if dfs(i, j + 2):
                    memo[(i, j)] = True
                    return True

                # Option 2: consume target from s
                if i < len(s) and (s[i] == target or target == "."):
                    if dfs(i + 1, j):
                        memo[(i, j)] = True
                        return True

                memo[(i, j)] = False
                return False

            # Normal character or '.'
            if i < len(s) and (s[i] == p[j] or p[j] == "."):
                res = dfs(i + 1, j + 1)
            else:
                res = False

            memo[(i, j)] = res
            return res

        return dfs(0, 0)

