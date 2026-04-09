class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        idx = 0
        while idx != len(s)-1:

            end = idx
            idx = min(len(s)-1, idx+maxJump)

            print(idx)

            while s[idx] == "1" and end+minJump <= idx:
                idx -= 1

            if idx < end+minJump:
                return False
        return True


