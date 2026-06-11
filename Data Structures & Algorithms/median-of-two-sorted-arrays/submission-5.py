class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
                 
        A = nums1
        B = nums2

        #enforce A is always smaller than B

        if len(B) < len(A):
            B, A = A, B

        total = len(A) + len(B)
        half = (total+1)//2

        l = 0 
        r = len(A)

        while l <= r:

            i = (l+r)//2 # the mid point for array A
            j = half -i # i+j make half of the joint array

            # i and j are pivot points

            A_left = A[i-1] if i > 0 else float('-inf')
            A_right = A[i] if i < len(A) else float('inf')

            B_left = B[j-1] if j > 0 else float('-inf')
            B_right = B[j] if j < len(B) else float('inf')

            # goal
            if A_left <= B_right and B_left <= A_right:

                if total%2 != 0:
                    #odd case
                    return max(A_left, B_left)
                else:
                    return (max(A_left, B_left)+min(A_right, B_right))/2
            else:
                if A_left > B_right:
                    #too many elements on A
                    r = i
                else:
                    l = i+1

