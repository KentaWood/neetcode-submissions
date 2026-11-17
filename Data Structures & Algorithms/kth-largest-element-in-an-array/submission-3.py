class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        counts = Counter(nums)
        h = []
        
        for num, freq in counts.items():
            heapq.heappush(h, (-num, freq))

        print(h)

        while k > 1:
            print(k)
            k -= heapq.heappop(h)[1]
        


        return -heapq.heappop(h)[0]