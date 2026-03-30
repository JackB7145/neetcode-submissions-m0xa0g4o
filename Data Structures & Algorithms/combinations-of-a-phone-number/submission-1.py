class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        reverse_keypad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []
        def dfs(idx, temp):
            if len(temp) == len(digits):
                res.append(temp)
                return
            for c in reverse_keypad[digits[idx]]:
                dfs(idx + 1, temp + c)
            

        if digits:
            dfs(0, "")


        return res