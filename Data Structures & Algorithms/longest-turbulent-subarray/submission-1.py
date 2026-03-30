class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        globalMax = 1
        localMax = 1

        # establish initial direction
        if arr[1] > arr[0]:
            greater = True
            localMax = 2
        elif arr[1] < arr[0]:
            greater = False
            localMax = 2
        else:
            greater = None  # equal case

        globalMax = localMax

        for i in range(1, len(arr) - 1):
            if arr[i] == arr[i+1]:
                localMax = 1
                greater = None
            elif (not greater and arr[i+1] > arr[i]) or (greater and arr[i+1] < arr[i]):
                # direction flipped → extend
                localMax += 1
                greater = not greater
            else:
                # direction didn't flip → start new pair
                localMax = 2
                greater = arr[i+1] > arr[i]

            globalMax = max(globalMax, localMax)

        return globalMax