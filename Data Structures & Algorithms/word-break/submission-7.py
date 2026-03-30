# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordSet = set(wordDict)
        # memo = {}

        # def traverse(idx):
        #     if idx in memo:
        #         return memo[idx]
        #     if idx == len(s):
        #         return True

        #     for i in range(idx, len(s)):
        #         if s[idx:i+1] in wordSet and traverse(i + 1):
        #             memo[idx] = True
        #             return True

        #     memo[idx] = False
        #     return False

        # return traverse(0)


        # '''
        # I got this question first try, but it was ineffiicent because of what I chose to memoize by. I chose to memoize by substring, meaning I'd keep track
        # the substrings meaning o(n^2) size in my memo, and when I had a substring that I new wasn't possible I new it didn't work. What was better is
        # to worry about start instead. If I memozied by the starting index idx, I could consistently and efificently determine which solutions have been seen before

        # '''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        bad = set()  # indices that are confirmed to NOT lead to a solution

        def traverse(idx):
            if idx in bad:
                return False
            if idx == len(s):
                return True

            for i in range(idx, len(s)):
                if s[idx:i+1] in wordSet and traverse(i + 1):
                    bad.add(i)  # only mark AFTER full failure
                    return True

            bad.add(idx)  # only mark AFTER full failure
            return False

        return traverse(0)