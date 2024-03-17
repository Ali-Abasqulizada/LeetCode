'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[n // 2]
    
#or
    
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        ans = {}
        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        n = len(nums) // 2
        for i in ans:
            if ans[i] > n:
                return i

#or
            
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        copy = 0
        for i in nums:
            if count == 0:
                copy = i
            if i == copy:
                count += 1
            else:
                count -= 1 
        return copy   
    
'''
Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''