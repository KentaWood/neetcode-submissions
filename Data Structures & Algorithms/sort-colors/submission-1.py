class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counts = [0,0,0]

        for num in nums:

            counts[num] += 1 

        
        
        color,i = 0,0 

        while color < 3 and i < len(nums):
            
            print(f"{counts}")
            
            if counts[color] == 0:
                color += 1
                continue 
            
            else:
                nums[i] = color 
                counts[color] -= 1 
                i += 1



        return None