class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = []
        ans2 = []

        seen1 = set(nums1)
        seen2 = set(nums2)

        for i in range(len(nums1)):

            if nums1[i] not in seen2:
                ans1.append(nums1[i])

            if nums2[i] not in seen1:
                ans2.append(nums2[i])
        
        return [list(set(ans1)),list(set(ans2))]