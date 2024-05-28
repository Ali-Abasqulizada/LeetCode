class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        check = {}
        for i in nums:
            check[i] = check.get(i, 0) + 1
        for i in check:
            if check[i] >= 2:
                return True
        return False