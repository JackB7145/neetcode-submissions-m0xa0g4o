class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for i in nums:
            dict1[i] += 1
        
        list1 = list(dict1.items())
        list1.sort(key=lambda a:a[1])
        solution = []
        for i in range(k):
            sol = list1.pop()
            solution.append(sol[0])
        return solution
