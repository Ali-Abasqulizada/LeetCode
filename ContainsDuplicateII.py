'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        check = {}
        for i in range(len(nums)):
            if nums[i] in check:
                if abs(check[nums[i]] - i) <= k:
                    return True
                else:
                    check[nums[i]] = i
            else:
                check[nums[i]] = i
        return False
            

'''
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''