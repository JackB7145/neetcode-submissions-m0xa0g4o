class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        onHand = {
            "20":0,
            "10":0,
            "5":0
        }

        for bill in bills:
            onHand[str(bill)] += 1
            given = bill
            given -= 5
            if not given:
                print(5)
                continue
            
            for amt in onHand:
                quantity = onHand[amt]
                print(amt, quantity, 'making', given)
                if given - int(amt) < 0:
                    continue
                
                if not quantity:
                    continue
                
                need = given // int(amt)
                given -= int(amt) * min(onHand[amt], need)
                onHand[amt] -= min(onHand[amt], need)

            if given:
                return False

        return True


            