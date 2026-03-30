class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []
        def traverse(integer, cnt):
            if cnt >= k:
                res.append(curr[:])
                return
            
            elif integer > n:
                return
            
            curr.append(integer)
            traverse(integer+1, cnt+1)
            curr.pop()
            traverse(integer+1, cnt)

        traverse(1, 0)
        return res