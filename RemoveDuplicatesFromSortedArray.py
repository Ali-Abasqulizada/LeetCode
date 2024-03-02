class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        uniqe = 0
        for i in nums:
            if nums[uniqe] != i:
                nums[uniqe + 1] = i
                uniqe += 1
        return uniqe + 1 