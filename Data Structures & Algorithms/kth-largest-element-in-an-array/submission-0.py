class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        arr = []

        heapq.heapify(arr)

        for i in nums:

            heapq.heappush(arr, -i)
        
        target = k
        
        while target > 1:

            heapq.heappop(arr)
            target-=1
        
        return -arr[0]
