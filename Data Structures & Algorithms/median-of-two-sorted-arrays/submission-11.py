class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
                 
        a = nums1
        b = nums2

        if len(a) > len(b):
            a, b = b , a # swap
        
        total = len(a)+len(b)

        half = total//2 

        if total%2 == 0:
            #even case
            half-=1

        i = half

        

        # asign left and right cursors to both a and b

        bl = float("inf") if i >= len(b) else b[i]
        br = float("inf") if i+1 >= len(b) else b[i+1]

        j = half-i
        al = float("-inf") if j-1 < 0 else a[j-1]
        ar = float("inf") if j >= len(a) else a[j]

        while True:

            if al <= br and bl <= ar:
                # left and right are divided
                break
            else:
                i-=1
                bl = float("-inf") if i < 0 else b[i]
                br = float("inf") if i+1 >= len(b) else b[i+1]

                j = half-i
                al = a[j-1]
                ar = float("inf") if j >= len(a) else a[j]
        print(al)
        print(bl)
        print(ar)
        print(br)

        
        if total%2 == 0:
            #even case
            left = max(al, bl)
            right = min(ar, br)
            return (left+right)/2
        else:
            return max(al, bl)




    
