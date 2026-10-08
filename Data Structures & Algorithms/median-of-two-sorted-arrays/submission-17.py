class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        a = nums1
        b = nums2
        total = len(a)+len(b)

        if len(a) > len(b):
            a , b = b , a

        # enforce length of a is greater than equal to b

        half = total//2 # the median of combined array
        
        i = half
        

        l = 0
        r = len(a)-1
        while True:
            i = (l + r) // 2  # Partition index for A
            j = half - i - 2  # Partition index for B

            la = float("-inf") if i < 0 else a[i]
            ra = float("inf") if i+1 > len(a)-1 else a[i+1]

            lb = float("-inf") if j < 0  else b[j]
            rb = float("inf") if j+1 > len(b)-1 else b[j+1]

            if la <= rb and lb <= ra:
                # l < r is true
                break

            elif la > rb:
                r = i - 1
            else:
                l = i + 1


        
        if total%2 == 0:

            left = max(la, lb)
            right = min(ra, rb)
            return (left+right)/2
        else:
            left = min(ra, rb)
            
            return left
