class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        ans = []

        def determineCorrectness(speed, h):
            p = piles.copy()

            index = 0
            for i in range(h):
                if index == len(p):
                    break
                else:
                    p[index] -= speed
                    if p[index] < 1:
                        index += 1
            num = 1 if index == len(p) else (0 if p[-1] < 1 else -1)

            if num == 1 and ans and ans[-1][0] > speed:
                ans.pop()
                ans.append((speed, num))
            elif not ans and num == 1:
                ans.append((speed, num))

            return num

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            correctness = determineCorrectness(mid, h)
            if correctness == 0:
                break
            elif correctness < 0:
                left = mid + 1
            else:
                right = mid - 1

        return ans[-1][0]
