class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = [(counts[k],k) for k in counts.keys()]

        print(f'{heap=}')

        heapq.heapify_max(heap)

        print(f'{heap=}')

        

        return [-1]

        