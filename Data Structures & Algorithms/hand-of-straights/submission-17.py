from collections import OrderedDict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        mp = OrderedDict()

        # Build the ordered dictionary
        for n in sorted(hand):
            mp[n] = mp.get(n, 0) + 1

        start = next(iter(mp))

        while mp:
            for n in range(start, start + groupSize):
                if n not in mp:
                    return False

                mp[n] -= 1

                if mp[n] == 0:
                    del mp[n]

            # Next smallest remaining number
            if mp:
                start = next(iter(mp))

        return True