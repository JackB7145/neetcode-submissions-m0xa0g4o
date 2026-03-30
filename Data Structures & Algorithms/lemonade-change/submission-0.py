class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        '''
        In summary:

        We get whatever bill they gave whether that is a 5, 10, or 20

        but if they give me than 5$ we need to give them back their change

        and we need to reutrn false of we don't have the bills
        '''

        arr = [0, 0, 0]

        def checkBills(money):
            while money:
                if money // 20 and arr[0]:
                    twenties = min(arr[0], money // 20)
                    money -= twenties * 20
                    arr[0] -= twenties
                elif money // 10 and arr[1]:
                    tens = min(arr[1], money // 10)
                    money -= tens * 10
                    arr[1] -= tens
                elif money // 5 and arr[2]:
                    fives = min(arr[2], money // 5)
                    money -= fives * 5
                    arr[2] -= fives
                else:
                    return False
            return True
            

        for payment in bills:
            idx = [20, 10, 5].index(payment)
            arr[idx] += 1
            payment -= 5
            if payment and not checkBills(payment):
                return False
        
        return True
                    