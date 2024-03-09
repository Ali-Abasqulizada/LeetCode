'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
                nums[i] = nums[i] * nums[i]
        return sorted(nums)
    
#or

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        count = len(nums) - 1
        ans = [0] * len(nums)
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                ans[count] = nums[right] * nums[right]
                right -= 1
            else:
                ans[count] = nums[left] * nums[left]
                left += 1
            count -= 1
        return ans

'''
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''