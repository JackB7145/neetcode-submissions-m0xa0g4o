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

        queue = deque(senate)

        removeR = 0
        removeD = 0

        mp = Counter(senate)

        while queue and mp["R"] != 0 and mp["D"] != 0:
            for _ in range(len(queue)):
                char = queue.popleft()
                if char == "R":
                    if removeR:
                        removeR -= 1
                        mp["R"] -= 1
                        continue
                    
                    removeD += 1

                else:
                    if removeD:
                        removeD -= 1
                        mp["D"] -= 1
                        continue
                    
                queue.append(char)
                    
        return "Radiant" if mp["D"] == 0 else "Dire"


            
