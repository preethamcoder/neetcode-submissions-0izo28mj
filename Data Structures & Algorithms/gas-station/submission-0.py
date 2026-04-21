class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1
        gas_total = 0
        res = 0
        length = len(gas)
        ind = 0
        for ind in range(length):
            gas_total += gas[ind]-cost[ind]
            if gas_total < 0:
                gas_total = 0
                res = ind+1
        return res