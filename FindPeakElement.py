'''
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. 
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
'''

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            if i < len(nums) - 1:
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    ans = i
            elif nums[-1] > nums[-2]:
                ans = len(nums) - 1
        return ans

#or

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        left = 1
        right = len(nums) - 2
        while left <= right:
            ave = (left + right) // 2
            if nums[ave] > nums[ave - 1] and nums[ave] > nums[ave + 1]:
                return ave
            elif nums[ave - 1] < nums[ave]:
                left = ave + 1
            else:
                right = ave - 1

'''
Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2
or index number 5 where the peak element is 6.
'''