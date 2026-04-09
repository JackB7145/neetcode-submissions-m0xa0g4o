class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        Can't I just build out the trust adj arr and just find the guy that has no one there?

        or no because everyone has to trust that guy

        this seems like the first node in topological sort?

        We count dead ends the one that has the most dead ends is the judge.

        But Im strill confusde on why I cant iterate throguh teh adj arr and find theone that trusts nobody. 

        Right, if there is only 1 person that satifies conditions 1 and 2. 

        rigth, 2 gurentees that everyone else must trust someone, since it must be the judge. 

        In fact if we fnid one person with length 1, we can even reutrn that? right

        okay so there might not be a town judge. So thats why it doesn't work, but... nooo, we can still reutrn -1 with my example I need more testcases

        '''


        adj = [[] for _ in range(n)]
        for a, b in trust:
            adj[a-1].append(b-1)
        
        for i in range(len(adj)):
            if len(adj[i]) == 0:
                return i + 1
        return -1

    