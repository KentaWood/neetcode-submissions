class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) -1 
        curr_max = 0

        while l < r:

            # len * wid for area len = r - l and wid = min of the two heights 
            area = (r - l) * min(heights[l],heights[r])
            curr_max = max(area, curr_max)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return curr_max




        