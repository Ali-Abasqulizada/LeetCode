class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points, key = lambda x : (x[0], x[1]))
        right = points[0][1]
        ans = 1
        for l, r in points[1:]:
            if right >= l:
                right = min(right, r)
            else:
                ans += 1
                right = r
        return ans