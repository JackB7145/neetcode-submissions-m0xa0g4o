class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        limit = total // k
        nums.sort(reverse=True)  # 🔥 critical

        subsets = [0] * k

        def backtrack(idx):
            if idx == len(nums):
                return True
            
            for i in range(k):
                # skip invalid
                if subsets[i] + nums[idx] > limit:
                    continue
                
                if i > 0 and subsets[i] == subsets[i - 1]:
                    continue
                
                subsets[i] += nums[idx]

                if backtrack(idx + 1):
                    return True

                subsets[i] -= nums[idx]

              
            
            return False
        
        return backtrack(0)