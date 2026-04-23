class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        
        left_prod = [1] * size
        right_prod = [1] * size
        ans = [0] * size
        
        for i in range(1, size):
            left_prod[i] = left_prod[i - 1] * nums[i - 1] 
            
        for i in range(size - 2, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i + 1]
            
        
        for i in range(0, size):
            ans[i] = left_prod[i] * right_prod[i]
        
        return ans