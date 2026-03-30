class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def checkDivisibility(string: str) -> bool:
            for i in range(len(str1)):
                if string[i % len(string)] != str1[i]:
                    return False
                
            for i in range(len(str2)):
                if string[i % len(string)] != str2[i]:
                    return False

            return True

        if str1[0] != str2[0]:
            return ""

        last = ""

        for i in range(min(len(str1), len(str2))):
            res = str1[:i + 1]

            # NEW: candidate length must divide both strings
            if len(str1) % len(res) != 0 or len(str2) % len(res) != 0:
                continue

            if checkDivisibility(res):
                last = res

        return last