class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([('0000', 0)])

        seen = set()
        deadends = set(deadends)

        while queue:
            curr, cnt = queue.popleft()

            if curr == target:
                return cnt
            
            if curr in deadends:
                continue

            seen.add(curr)
            temp = list(curr)
            for idx in range(4):
                digit = int(curr[idx])

                for change in [1, -1]:
                    new_digit = (digit + change) % 10

                    temp = list(curr)
                    temp[idx] = str(new_digit)
                    newString = ''.join(temp)

                    if newString not in seen and newString not in deadends:
                        seen.add(newString)
                        queue.append((newString, cnt + 1))

        
        return -1
            


            
