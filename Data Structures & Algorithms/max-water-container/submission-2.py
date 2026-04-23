class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        
        while(l < r):
            l_num = heights[l]
            r_num = heights[r]
            
            # print(l_num)
            # print(r_num)
            
            area = min(l_num, r_num) * (r - l)
            
            max_area = max(max_area, area)
            
            if l_num > r_num:
                r -= 1
            else:
                l += 1
                
            
        return max_area