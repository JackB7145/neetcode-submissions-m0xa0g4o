class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        We need to return all teh ways we cna partrition hte string so that each substring genereated is a valid palendrome:

        - Where the substring is the same as when its reversed

        Ideas:

        1. I could validate by if a string is a palendrome with o(20) or cosntant time if I know the length is between 1 and 20

        if we find that a current substring is a palendrome, we move the starting index over and start again from 1 over and we keep going

        '''
        res = []
        temp = []

        def isPalendrome(substring):
            l, r = 0, len(substring)-1

            while l < r:
                if substring[l] != substring[r]:
                    return False
                
                l += 1
                r -= 1

            return True

        def partition(idx):
            if idx >= len(s):
                res.append(temp[:])
                return

            string = ""
            for i in range(idx, len(s)):
                string += s[i]
                if isPalendrome(string):
                    temp.append(string)
                    partition(i+1)
                    temp.pop()


        partition(0)
        return res
                

            