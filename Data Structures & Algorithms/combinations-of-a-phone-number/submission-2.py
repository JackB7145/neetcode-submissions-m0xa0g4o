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
        temp = [] 
        def backtrack(idx):
            if idx >= len(digits):
                string = ''.join(temp[:])
                if string:
                    res.append(string)
                return
            
            for c in reverse_keypad[digits[idx]]:
                temp.append(c)
                backtrack(idx+1)
                temp.pop()
            
        backtrack(0)
        return res