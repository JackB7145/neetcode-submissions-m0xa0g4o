class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        highest = 0
        for i in range(len(heights)):
            print(stack, heights[i])
            if stack and heights[i]<=stack[-1][0]:
                areaLarger = heights[i] * (stack[-1][1] + 1) >= stack[-1][0] * stack[-1][1]

                print("Inside smaller than prior: ", areaLarger, heights[i], stack[-1][0])
                data = stack.pop()
                if areaLarger:
                    stack.append((heights[i], data[1]+1))
                else:
                    stack.append((heights[i], 2))
            elif stack:
                areaLarger = stack[-1][0] * (stack[-1][1] + 1) > heights[i]
                print("Inside larger than prior: ", areaLarger)
                data = stack.pop()
                if areaLarger:
                    stack.append((data[0], data[1]+1))
                else:
                    stack.append((heights[i], 1))
            
            else:
                stack.append((heights[i], 1))
        data = stack.pop()
        return data[0] * (data[1]) 