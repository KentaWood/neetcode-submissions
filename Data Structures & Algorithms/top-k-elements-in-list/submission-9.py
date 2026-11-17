class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
            if len(count) <= k:
                continue
            
            new_count = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    new_count[num] = c - 1
            # print(new_cou`kknt.items())
            count = new_count
        
        res = []

        print("Here:",  count)
        
        for num in count:
                res.append(num)
        
        return res