class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        start = 0
        surplus = gas[0] - cost[0]

        # Step 1: Find index with max surplus
        for i in range(1, len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            if diff > surplus:
                surplus = diff
                start = i

        # Step 2: Try to simulate from that start index
        tank = 0
        n = len(gas)
        for i in range(n):
            idx = (start + i) % n
            tank += gas[idx] - cost[idx]
            if tank < 0:
                return -1  # can't complete circuit

        return start
