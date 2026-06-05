class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        while l < r:

            k = l+(r-l)//2

            time = sum(math.ceil(pile / k) for pile in piles)

            if time <= h:

                r = k
            else:
                l = k+1
        
        return l

                 