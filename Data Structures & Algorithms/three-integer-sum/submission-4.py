class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = sorted(nums)
        ans = []

        for i, num in enumerate(n):

            if num > 0:
                break
            
            if i > 0 and n[i] == n[i - 1]:
                continue
            # print(num)

            target = 0 - num

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = n[l] + n[r]

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    
                    ans.append([num, n[l], n[r]])

                    l += 1
                    r -= 1

                    while l < r and n[l] == n[l - 1]:
                        l += 1
                
        return ans


        