class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ans = 0
        check = float("inf")
        nums.sort()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total
                elif total > target:
                    r -= 1
                else:
                    l += 1
                diff = abs(total - target)
                if diff < check:
                    check = diff
                    ans = total
        return ans