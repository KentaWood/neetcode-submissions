class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        sorted_nums = sorted(nums)
        prev = None
        size = len(nums)
        print(sorted_nums)
        
        
        for i in range(size - 2):
            if sorted_nums[i] == prev:
                pass
            
            else:
                l = i
                r = size - 1
                find = 0 - sorted_nums[i]
                # print(find)
                # print(ans)
                
                while(l < r):
                    sum = sorted_nums[l] + sorted_nums[r]
                    # print("here")
                    # print(sorted_nums[l])
                    # print(sorted_nums[r])
                    
                    if sum == find:
                        # print("here2")
                        ans.append([sorted_nums[i],sorted_nums[l],sorted_nums[r]])
                        r -= 1
                    elif sum > find:
                        r -= 1
                    else:
                        l += 1
                    
            prev = sorted_nums[i]    

        return ans