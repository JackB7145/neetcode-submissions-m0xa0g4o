class Solution:
    def trap(self, height: List[int]) -> int:
        r = 0
        water = 0
        
        for i in range(len(height)-1):
            
            if i < r:
                continue 

            r = i + 1

            temp = 0
            highest = (0,0)
            while height[r] < height[i]:
                if highest[0] < height[r]:
                    highest = (height[r], r)

                temp += height[i] - height[r]
                r += 1

                if r == len(height):
                    print(highest, r-1)
                    temp = 0 if highest[0] > height[len(height)-1] or r-1 - i < 2 else temp - (height[i] - highest[0]) * (highest[1] - i - 1)
                    print(f'Left side Block: {height[i]}, Right side Block: {height[r-1]}, Temp: {temp}')
                    r = i + 1
                    
                    break


            # print(f'Left side Block: {height[i]}, Right side Block: {height[r]}, Temp: {temp}')

            water += temp 

        
        return water