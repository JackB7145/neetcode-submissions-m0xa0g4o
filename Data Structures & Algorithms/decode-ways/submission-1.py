class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        prev2 = 1  # ways to decode empty prefix
        prev = 1   # ways to decode first character

        for i in range(1, len(s)):
            curr = 0

            # Single digit
            if s[i] != "0":
                curr += prev

            # Two digits (this DOES handle "10")
            if 10 <= int(s[i-1:i+1]) <= 26:
                curr += prev2

            prev2 = prev
            prev = curr

        return prev
