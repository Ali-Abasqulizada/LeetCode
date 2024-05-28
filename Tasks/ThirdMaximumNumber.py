class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        check = set(nums)
        check = sorted(check)
        if len(check) < 3:
            return check[-1]
        return check[-3]

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