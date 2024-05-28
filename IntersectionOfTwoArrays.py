'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.
'''

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        check1 = set(nums1)
        check2 = set(nums2)
        ans = []
        for i in check1:
            if i in check2:
                ans.append(i)
        return ans

#or
    
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        check = {}
        ans = []
        for i in nums1:
            check[i] = 1
        for i in nums2:
            if i in check and check[i] == 1:
                ans.append(i)
                check[i] -= 1
        return ans

#or

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        check1, check2 = set(nums1), set(nums2)
        check1 = sorted(check1)
        check2 = sorted(check2)
        i, j = 0, 0
        ans = []
        while i < len(check1) and j < len(check2):
            if check1[i] == check2[j]:
                ans.append(check1[i])
                i += 1
                j += 1
            elif check1[i] > check2[j]:
                j += 1
            else:
                i += 1
        return ans

'''
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''