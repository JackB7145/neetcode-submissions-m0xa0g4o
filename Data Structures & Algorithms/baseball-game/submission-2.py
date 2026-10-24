class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for n in operations:
            if n == "+":
                record.append(record[-1]+record[-2])
            elif n == "C":
                record.pop()
            elif n == "D":
                record.append(2*record[-1])
            else:
                record.append(int(n))
        
        return sum(record)
        