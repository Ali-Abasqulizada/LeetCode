'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = {}
        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        for i in ans:
            if ans[i] == 1:
                return i
            
#or
            
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
            
#or
            
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
    
'''
Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1
'''