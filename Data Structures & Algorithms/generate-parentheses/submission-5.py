class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []    
        string = []

        def backtrack(openB, closedB):
            if openB + closedB == n*2:
                res.append(''.join(string[:]))
                return
            
            if openB < n:
                string.append("(")
                backtrack(openB+1, closedB)
                string.pop()
            
            if openB > closedB:
                string.append(')')
                backtrack(openB, closedB+1)
                string.pop()
                        
        backtrack(0, 0)
        return res
