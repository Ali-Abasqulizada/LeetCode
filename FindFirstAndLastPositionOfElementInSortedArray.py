'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                start, end = m, m
                while end + 1 < len(nums) and nums[end + 1] == target:
                    end += 1
                while start - 1 >= 0 and nums[start - 1] == target:
                    start -= 1
                return [start, end]
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [-1, -1]

'''
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''