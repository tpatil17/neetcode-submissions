from functools import cache

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start = 0
        tank = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            tank+=gas[i]
            tank-=cost[i]

            while tank < 0:
                tank+=cost[start]
                tank-=gas[start]
                start+=1

                if start > len(gas)-1:
                    return -1
        
        return start
        
