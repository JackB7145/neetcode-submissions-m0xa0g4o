class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        '''
        What this sounds like to me is essentially keeping track of the majority and return once we know we've lost

        there seems to be a priority and relationship between the order of arrival versus quantity

        why can't i do a linear traversal

        keeping track of momentum if we hit a radiant

        they always cancel dires right.

        same with dire

        lets model that relationship with a simple counter for refereence

        we hit radiant we add 1

        we hit dire we subtract 1

        the side its most lenient on it means we have cancelled more of their votes

        and we take the other?

        but there needs to be two counters

        because in the first example with RRDDD

        right DD woun't subtract from that

        so their needs to be a counter for momentum and a count for result


        '''

        momentum = 0
        result = 0

        for senator in senate:
            print(senator, momentum, result)
            if senator == "R":
                if momentum >= 0:
                    result += 1
                    momentum += 1
                else:
                    momentum += 1

            else:
                if momentum <= 0:
                    result -= 1
                    momentum -= 1
                else:
                    momentum -= 1
        
        return "Radiant" if result > 0 else "Dire"