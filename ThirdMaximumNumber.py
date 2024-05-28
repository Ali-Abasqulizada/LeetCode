'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, 
return the maximum number.
'''

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        check = set(nums)
        check = sorted(check)
        if len(check) < 3:
            return check[-1]
        return check[-3]

#or

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        I, II, III = None, None, None
        for i in nums:
            if I == i or II == i or III == i:
                continue
            elif I == None or i > I:
                III = II
                II = I
                I = i
            elif II == None or i > II:
                III = II
                II = i
            elif III == None or i > III:
                III = i
        return I if III == None else III

'''
Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''