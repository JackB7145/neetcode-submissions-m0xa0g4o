class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            # word1 is exhausted:
            # insert all remaining characters from word2
            if i == len(word1):
                return len(word2) - j

            # word2 is exhausted:
            # delete all remaining characters from word1
            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            # Characters already match
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)

            else:
                # Delete word1[i]
                delete = dfs(i + 1, j)

                # Insert word2[j]
                insert = dfs(i, j + 1)

                # Replace word1[i] with word2[j]
                replace = dfs(i + 1, j + 1)

                memo[(i, j)] = 1 + min(delete, insert, replace)

            return memo[(i, j)]

        return dfs(0, 0)
