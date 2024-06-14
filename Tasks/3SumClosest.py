class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans = 0
        diff = float("inf")
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
                check = abs(total - target)
                if check < diff:
                    diff = check
                    ans = total
        return ans