class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []    

        string = []

        def backtrack(openBrackets):
            if len(string) >= n*2 and openBrackets != 0:
                return

            if len(string) == n*2:
                res.append(''.join(string[:]))
                return


            if openBrackets < n:
                string.append('(')
                backtrack(openBrackets+1)
                string.pop()
            if openBrackets > 0:
                string.append(')')
                backtrack(openBrackets-1)
                string.pop()
                        
        backtrack(0)
        return res
