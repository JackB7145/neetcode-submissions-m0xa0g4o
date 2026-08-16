class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = Counter(s)

        currLength = 0
        res = []
        loadedCount = {} 

        '''
        res = [5, 5, 1, 1, 1]

        loadedCount: 

        {
        }
        '''

        for c in s:
            currLength += 1 #0
            if c in loadedCount:
                loadedCount[c] -= 1
                if not loadedCount[c]:
                    del loadedCount[c]

            else:
                if cnt[c] - 1 != 0:
                    loadedCount[c] = cnt[c]-1

            if len(loadedCount) == 0:
                res.append(currLength)
                currLength = 0
        
        return res

            