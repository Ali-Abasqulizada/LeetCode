class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        ans = [0] * len(nums)
        i = len(nums) - 1
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                ans[i] = nums[l] * nums[l]
                l += 1
            else:
                ans[i] = nums[r] * nums[r]
                r -= 1
            i -= 1
        return ans