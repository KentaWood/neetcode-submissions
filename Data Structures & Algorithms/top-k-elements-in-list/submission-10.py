from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()

        for num in nums:
            if num in count:
                count[num] += 1
            elif len(count) < k:
                count[num] = 1
            else:
                # Decrease all counts by 1
                to_remove = []
                for key in count:
                    count[key] -= 1
                    if count[key] == 0:
                        to_remove.append(key)
                for key in to_remove:
                    del count[key]

        # Second pass to verify real top-k
        real_count = defaultdict(int)
        for num in nums:
            if num in count:
                real_count[num] += 1

        # Sort final candidates by actual frequency
        result = sorted(real_count.keys(), key=lambda x: -real_count[x])
        return result[:k]
