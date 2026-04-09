class Solution:
    def trap(self, height: List[int]) -> int:
        r = 0
        water = 0
        
        for i in range(len(height)-1):
            
            if i < r:
                continue 

            r = i + 1

            temp = 0
            while height[r] < height[i]:
                temp += height[i] - height[r]
                r += 1
                if r == len(height):
                    break

            print(f'Left side Block: {height[i]}, Right side Block: index r, Temp: {temp}')

            water += temp if r != len(height) else 0

        
        return water