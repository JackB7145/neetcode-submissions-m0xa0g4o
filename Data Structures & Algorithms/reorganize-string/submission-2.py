class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        maxHeap = [(-cnt[c], c) for c in cnt]

        heapq.heapify(maxHeap)

        string = []
        queue = deque()
        while maxHeap:
            
            curr = heapq.heappop(maxHeap)
            freq, char = curr

            if string and string[-1] == char:
                return ""

            string.append(char)

            if queue:
                f, c = queue.popleft()
                heapq.heappush(maxHeap, (f, c))

            if freq + 1 < 0:
                queue.append((freq+1, char))

        if queue:
            return ""
        return "".join(string)

