class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        check = max(nums)
        ans = 0
        for i in range(len(nums)):
            if nums[i] == check:
                ans = i
            elif check < 2 * nums[i]:
                return -1
        return ans