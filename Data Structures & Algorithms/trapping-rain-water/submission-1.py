class Solution:
    def trap(self, height: List[int]) -> int:
        r = 0
        water = 0
        
        for i in range(len(height)):
            
            if i < r:
                continue 

            r = i + 1

            temp = 0
            while height[r] < height[i]:
                temp += height[i] - height[r]
                r += 1
                print(r)
                if r == len(height):
                    break

            water += temp if r != len(height) else 0

        
        return water