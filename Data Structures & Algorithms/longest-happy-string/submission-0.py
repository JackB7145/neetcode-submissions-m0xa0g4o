class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        string = []
        heap = []
        for cnt, character in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt < 0:
                heap.append((cnt, character))

        heapq.heapify(heap)

        while heap:
            curr = heapq.heappop(heap)
            freq, char = curr

            if len(string) > 1 and string[-1] == string[-2] == char:
                if not heap:
                    break
                
                newCurr = heapq.heappop(heap)
                f, c = newCurr

                string.append(c)
                if f + 1 < 0:
                    heapq.heappush(heap, (f+1, c))
                
                heapq.heappush(heap, (freq, char))
            
            else:
                string.append(char)
                if freq + 1 < 0:
                    heapq.heappush(heap, (freq+1, char))

        
        return ''.join(string)


