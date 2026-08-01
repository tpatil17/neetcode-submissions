class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        alt = [-nums for nums in stones]
        
        heapq.heapify(alt)

        
       
        while len(alt) > 1:

            x = -heapq.heappop(alt)

            y = -heapq.heappop(alt)

            if x > y:
                new = x-y
                heapq.heappush(alt, -new)
            elif y > x:
                new = y-x
                heapq.heappush(alt, -new)
        
        if len(alt) == 0:
            return 0
        else:
            return -alt[0]

            