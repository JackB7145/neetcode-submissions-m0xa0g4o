class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(items, a, b):
            temp = items[a]
            items[a] = items[b]
            items[b] = temp

        def insertion_sort(items):
            for i in range(1, len(items)):
                for j in range(i - 1, -1, -1):
                    if items[j] > items[j + 1]:
                        swap(items, j, j + 1)
                    else:
                        break
            return items

        return insertion_sort(nums)
