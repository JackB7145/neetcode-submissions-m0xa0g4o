from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = defaultdict(int)
        for num in hand:
            count[num] += 1

        hand.sort()
        for num in hand:
            # Only try to build a group starting at `num` if it hasn't been used yet
            if count[num] == 0:
                continue
            # Try to build group from num to num + groupSize - 1
            for i in range(num, num + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1

        return True
