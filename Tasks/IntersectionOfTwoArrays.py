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