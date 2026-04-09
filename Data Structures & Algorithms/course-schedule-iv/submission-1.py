class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        This isn't topological sort, because we arn't traverding. 

        It's a dfs ago traversing a adj matrix

        we just need to keep track of that.

        That's not to bad

        But with just that there is a lot of rahandling logic

        for example with a > b > c > d

        we can if we want a d ? which is true, then we ask a c ? but now we have to re traverse

        We could keep a per node connectivity mp as well which is node: set() logic

        Thats a further optimization


        '''

        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
    

        inPath = set()
        def traverse(curr, end):
            if curr == end:
                return True
            
            elif curr in inPath:
                return False
            
            res = False
            inPath.add(curr)
            for node in adj[curr]:
                res = res or traverse(node, end)

                if res:
                    return res
                
            return False
            inPath.remove(curr)
        
        ans = []
        for start, end in queries:
            ans.append(traverse(start, end))
        
        return ans
            



