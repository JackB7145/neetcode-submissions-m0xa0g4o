class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        def backtrack(balance):
            if len(temp[:]) == n*2 and balance == 0:
                res.append(''.join(temp[:]))
                return
            
            if balance < 0 or len(temp[:]) > n * 2:
                return
            
            temp.append('(')
            backtrack(balance+1)
            temp.pop()
            temp.append(')')
            backtrack(balance-1)
            temp.pop()
       
            
        backtrack(0)
        return res