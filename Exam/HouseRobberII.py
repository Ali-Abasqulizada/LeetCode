from functools import cache
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def find1(i):
            if i >= len(nums):
                return 0
            return max(find1(i + 1), find1(i + 2) + nums[i])
        @cache
        def find2(i):
            if i < 0:
                return 0
            return max(find2(i - 1), find2(i - 2) + nums[i])
        return max(find1(1), find2(len(nums) - 2))
    
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def find(arr):
            l, r = 0, 0
            for i in arr:
                l, r = r, max(r, l + i)
            return r
        return max(find(nums[1:]), find(nums[:-1]))