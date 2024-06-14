class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        ans = 0
        for i in range(mid):
            ans += nums[mid] - nums[i]
        for i in range(mid + 1, len(nums)):
            ans += nums[i] - nums[mid]
        return ans