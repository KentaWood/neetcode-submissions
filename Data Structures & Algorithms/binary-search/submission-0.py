class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
         
        while(l <= r ):
            index = (l + r) // 2
            find = nums[index] 
            
            if find == target:
                return index 
            elif find > target:
                r = index - 1
            else:
                l = index + 1
        
        return -1    
    