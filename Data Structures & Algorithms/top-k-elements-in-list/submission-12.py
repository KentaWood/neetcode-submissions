class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        res = []
        freq = [0] * len(nums)



        
        
        