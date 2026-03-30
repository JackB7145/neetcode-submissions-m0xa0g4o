class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Keep a map of all the characters indexes in s

        Then find the minimum and maximum distances and splice the string for your answer

        What happens if there are multiple of each character, 


        I'm gonna cheat a little by knowing it's supposed to be a sliding window

        Say we wanted to use sliding window:

        what if we iterate over and every time we see a new chracter that we need we replace the existing one
        '''


        need = Counter(t)
        mp = defaultdict(list)
        res = (float('-inf'), float('inf'))
        def compare():
            for c in need:
                if c not in mp or len(mp[c]) < need[c]:
                    return False
            return True

        for i, c in enumerate(s):
            if c in need:
                mp[c].append(i)
                if len(mp[c]) > need[c]:
                    mp[c] = mp[c][1:]

            if compare():
                smallest, largest = float('inf'), float('-inf')
                for key in mp:
                    smallest = min(smallest, mp[key][0])
                    largest = max(largest, mp[key][-1])
                
                if largest-smallest < res[1]-res[0]:
                    res = (smallest, largest)
        
        if res[1]-res[0] > len(s):
            return ""
        return s[res[0]:res[1]+1]
                


            
