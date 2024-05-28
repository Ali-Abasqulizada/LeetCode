class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
    
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        ans = 0
        count = 0
        for i in nums:
            if count == 0:
                ans = i
            if ans == i:
                count += 1
            else:
                count -= 1
        return ans