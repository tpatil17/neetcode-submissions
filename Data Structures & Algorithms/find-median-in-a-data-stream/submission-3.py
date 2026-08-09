class MedianFinder:

    def __init__(self):

        self.lo = []
        self.hi = []

        heapq.heapify(self.lo) #max heap
        heapq.heapify(self.hi) #min heap
        

    def addNum(self, num: int) -> None:

        if not self.lo and not self.hi:
            heapq.heappush(self.lo,-num)
            return
        else:
            if num > -self.lo[0]: #put it in the hi pile
                heapq.heappush(self.hi, num)
            else:
                heapq.heappush(self.lo, -num)
            
            if not len(self.lo) >= len(self.hi):
                carry = heapq.heappop(self.hi)
                heapq.heappush(self.lo, -carry)
            else:             
                if len(self.lo) - len(self.hi) >1:
                    carry = heapq.heappop(self.lo)
                    heapq.heappush(self.hi, -carry)
            return 

        

    def findMedian(self) -> float:

        if len(self.lo)==len(self.hi):
            return (-self.lo[0] + self.hi[0])/2
        else:
            return -self.lo[0]
        
   