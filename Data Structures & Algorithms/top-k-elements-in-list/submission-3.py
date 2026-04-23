class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = Counter(nums)
        list_counts = [(-v, k) for k,v in counts.items()]

        heapq.heapify(list_counts)

        for _ in range(k):
            res.append(heapq.heappop(list_counts)[1])

        return res