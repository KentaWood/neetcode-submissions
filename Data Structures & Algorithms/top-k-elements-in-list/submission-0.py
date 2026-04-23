class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_freq = {}

        for num in nums:
            if num not in num_freq:
                num_freq[num] = 1
            else:
                num_freq[num] += 1
        
        sorted_data = sorted(num_freq, key=lambda x: num_freq[x], reverse=True)

        print(sorted_data)
        return sorted_data[:k]