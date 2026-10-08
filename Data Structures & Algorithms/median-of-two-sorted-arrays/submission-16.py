class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        a = nums1
        b = nums2
        total = len(a)+len(b)

        if len(b) > len(a):
            a , b = b , a

        # enforce length of a is greater than equal to b

        half = total//2 # the median of combined array
     
        if total%2 ==0:
            # even case
            half-=1
        
        i = half
        

        la = a[i]
        ra = float("inf") if i+1 > len(a)-1 else a[i+1]

        j = half - i
        lb = float("-inf") if j-1 < 0 else b[j-1]
        rb = float("inf") if j > len(b)-1 else b[j]

        while True:

            if la <= rb and lb <= ra:
                # l < r is true
                break
            else:

                i-=1
                j = half-i

                la = float("-inf") if i < 0 else a[i]
                ra = a[i+1]

                lb = float("inf") if j-1 > len(b)-1 else b[j-1]
                rb = float("inf") if j > len(b)-1 else b[j]
        
        print(la)
        print(ra)
        print(lb)
        print(rb)

        
        if total%2 == 0:

            l = max(la, lb)
            r = min(ra, rb)
            return (l+r)/2
        else:
            l = max(la, lb)
            
            return l
