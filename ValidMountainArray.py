'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
'''

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        up = True
        down = False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            elif arr[i] > arr[i - 1] and up:
                down = True
            elif arr[i] < arr[i - 1] and down:
                up = False
            else:
                return False
        if not up and down:
            return True
        return False

'''
Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true
'''