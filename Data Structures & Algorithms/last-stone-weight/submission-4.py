class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)

        print(f"HERE: {stones}")

        while len(stones) > 1:

            f_heavy = heapq.heappop_max(stones)
            s_heavy = heapq.heappop_max(stones)

            if f_heavy != s_heavy:
                heapq.heappush_max(stones, f_heavy - s_heavy)

            print(stones)

        return stones[0] if stones else 0







        # stones.sort()

        # while len(stones) > 1:

        #     hs_1 = stones[-1]
        #     hs_2 = stones[-2]
            
        #     #either way get rid of the weights
        #     stones.pop()
        #     stones.pop()

        #     if hs_1 != hs_2:
        #         stones.append(hs_1 - hs_2)
            
        #     stones.sort()
            
        #     print(stones)

        # return stones[0] if stones else 0
        