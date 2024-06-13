'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
'''

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        check = {}
        ans = []
        last = []
        for i in arr1:
            check[i] = check.get(i, 0) + 1
        for i in arr2:
            while check[i]:
                check[i] -= 1
                ans.append(i)
        for i in check:
            while check[i]:
                check[i] -= 1
                last.append(i)
        last.sort()
        return ans + last

'''
Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
'''