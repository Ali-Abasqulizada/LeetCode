'''
Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        check = 1
        zero = 0
        index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                index = i
            else:
                check *= nums[i]
        if zero >= 2:
            return ans
        if zero == 1:
            ans[index] = check
            return ans
        for i in range(len(nums)):
            ans[i] = check // nums[i]
        return ans
    
#or
    
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1] * len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            ans[i] *= left
            left *= nums[i]
            ans[len(nums) - i- 1] *= right
            right *= nums[len(nums) - i - 1]
        return ans
    
'''
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''