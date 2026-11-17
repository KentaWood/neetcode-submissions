class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        counts = Counter(nums)
        h = []
        
        for num, freq in counts.items():
            heapq.heappush(h, (freq, num))

        print(h)

        return -1