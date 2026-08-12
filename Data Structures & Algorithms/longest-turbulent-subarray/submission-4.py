class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        cnt = 1
        res = 1
        needsBigger = None

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                if needsBigger == True:
                    # Correct alternating comparison
                    cnt += 1
                else:
                    # Start a new turbulent subarray
                    cnt = 2

                needsBigger = False

            elif arr[i] < arr[i - 1]:
                if needsBigger == False:
                    # Correct alternating comparison
                    cnt += 1
                else:
                    # Start a new turbulent subarray
                    cnt = 2

                needsBigger = True

            else:
                cnt = 1
                needsBigger = None

            res = max(res, cnt)

        return res