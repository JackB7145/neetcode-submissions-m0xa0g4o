class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        blockedDire, totalDire = 0, 0
        blockedRadiant, totalRadiant = 0, 0

        mp = Counter(senate)
        
        while True:
            blockedDire = totalDire
            blockedRadient = totalRadiant

            if blockedRadient >= mp["R"]:
                return "Dire"
            
            elif blockedDire >= mp['D']:
                return "Radiant"
                
            for c in senate:
                if c == "R":
                    if blockedRadiant:
                        blockedRadiant -= 1
                        continue
                    else:
                        blockedDire += 1
                        totalDire += 1
                    
                else:
                    if blockedDire:
                        blockedDire -= 1
                        continue
                    
                    else:
                        blockedRadiant += 1
                        totalRadiant += 1
                    

                    
                

                