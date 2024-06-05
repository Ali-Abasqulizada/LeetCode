class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = [intervals[0]]
        for l, r in intervals[1:]:
            pl, pr = ans[-1]
            if l <= pr and r <= pr:
                continue
            elif l <= pr:
                ans.pop()
                ans.append([pl, r])
            else:
                ans.append([l, r])
        return ans