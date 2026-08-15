class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        Our first step is to start to build a hand

        so grab the smallest one, then see if we have the next, then the next, then the next, then restart when we have met the hand limit

        is there a way we can check if we have the number in o(1) lookup and also keep track of the order and count

        ordered dict or hashmap

        we will try hashmap first
        '''

        if len(hand) % groupSize != 0:
            return False
        
        mp = {}
        start = 10**9
        for n in hand:
            mp[n] = mp.get(n, 0) + 1
            start = min(n, start)
        
        possibleHands = len(hand) / groupSize
        hands = 1

        while hands <= possibleHands:
            tempStart = 10**9
            for n in range(start, start+groupSize):
                if n in mp and mp[n] > 0:
                    mp[n] -= 1
                    if mp[n] != 0:
                        tempStart = min(tempStart, n)
                    else:
                        del mp[n]
                        
                else:
                    return False

            hands+=1
            start = tempStart
            if start >= 10**9:
                start = min(mp) if mp else 0

        return True

        