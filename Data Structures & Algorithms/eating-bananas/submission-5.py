class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        pile_len = len(piles)

        hi_pile = max(piles) #in case h matches pile_len

        l = 1
        k = l + (hi_pile - l)//2
        

        while l < hi_pile:

            cost = 0
            for i in range(len(piles)):

                if piles[i] < k:
                    cost+=1
                elif piles[i] % k == 0:
                    cost+= piles[i]//k
                else:
                    cost+= (piles[i]//k)+1
            
            if cost <= h:

                #optimal
                hi_pile = k # reduce the max needed to k
            else:
                
                l = k+1
            
            k = l+(hi_pile-l)//2
        
        return k







