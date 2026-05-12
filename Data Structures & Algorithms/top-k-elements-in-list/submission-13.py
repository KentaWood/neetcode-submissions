class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        res = []
        # the index of this is the freq so freq[freq] = num
        freq = [[] for _ in range(len(nums) + 1)]


        for key,v in counts.items():
            freq[v].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                print(res,len(res), k)

                if len(res) == k:
                    return res
            



        
        
        