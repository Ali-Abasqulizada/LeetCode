'''
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits 
and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, 
with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 
are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using 
their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. 
If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 
is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1, n2 = 0, 0
        while n1 < len(version1) and n2 < len(version2):
            num1, num2 = "0", "0"
            for i in range(n1, len(version1)):
                if version1[i] == ".":
                    n1 = i + 1
                    break
                num1 += version1[i]
                if i == len(version1) - 1:
                    n1 = i + 1
                    break
            for i in range(n2, len(version2)):
                if version2[i] == ".":
                    n2 = i + 1
                    break
                num2 += version2[i]
                if i == len(version2) - 1:
                    n2 = i + 1
                    break
            if int(num1) > int(num2):
                return 1
            elif int(num1) < int(num2):
                return -1
        for i in range(n1, len(version1)):
            if version1[i] in "123456789":
                return 1
        for i in range(n2, len(version2)):
            if version2[i] in "123456789":
                return -1
        return 0

'''
Example 1:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 2:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".

Example 3:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
'''