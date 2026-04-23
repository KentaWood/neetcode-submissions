class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        curr_max = 0

        while l < r:
            lh, rh = heights[l], heights[r]

            curr_max = max(curr_max, (r - l ) * min(lh, rh))

            if lh > rh:
                r -= 1
            else:
                l += 1
        return curr_max

        