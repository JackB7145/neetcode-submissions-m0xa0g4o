class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        Count characters, put it in a heap

        and somehow we need to separate it

        we need the largest counts the most separated right, 

        its like I need to alternate between minimum count and maximimum count
        
        '''
        n = len(s)
        mp = Counter(s)
        heap = []
        
        for key in mp:
            heapq.heappush(heap, (-mp[key], key))
        
        res = []
        lastUsed = heapq.heappop(heap)
        res.append(lastUsed[1])
        
        # decrease count immediately since we used it
        lastUsed = (lastUsed[0] + 1, lastUsed[1])
        if lastUsed[0] == 0:
            lastUsed = None
        
        while len(res) < n:
            if not heap:
                return ""
            node = heapq.heappop(heap)
            res.append(node[1])
            
            # only push lastUsed back if it still exists
            if lastUsed is not None:
                heapq.heappush(heap, lastUsed)
            
            # update current node count
            lastUsed = (node[0] + 1, node[1])
            
            # if count becomes zero, clear it
            if lastUsed[0] == 0:
                lastUsed = None
            
            if len(res) > 1 and res[-1] == res[-2]:
                return ""
        
        return "".join(res)