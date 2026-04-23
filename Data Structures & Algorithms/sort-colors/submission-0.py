class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = Counter(nums)

        print(counts)
        
        p = 0
        for i in range(3):

            if i in counts:
                for j in range(counts[i]):

                    nums[p] = i

                    p += 1
        
        
        