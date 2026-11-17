class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start = 0
        curr_max = 0
        total = 0

        for  i in range(len(gas)):

            start = i if curr_max < gas[i] - cost[i] else start
            curr_max = gas[i] - cost[i] if curr_max < gas[i] - cost[i] else curr_max
            total += gas[i] - cost[i]


        return start if total >= 0 else -1 

        