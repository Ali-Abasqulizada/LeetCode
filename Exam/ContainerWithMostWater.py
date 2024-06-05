class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            cur = min(height[left], height[right]) * (right - left)
            ans = max(ans, cur)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans