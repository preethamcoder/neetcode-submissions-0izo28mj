class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        # Make A be the smaller array for simpler tracking
        if len(A) > len(B):
            A, B = B, A
        lA = len(A)
        lB = len(B)
        total = lA + lB
        half = total // 2
        l = 0
        r = lA - 1
        # Now, we find the median
        while True:
            midA = (l+r)//2
            midB = half-midA-2
            # get mids of both arrays
            Aleft = A[midA] if midA >= 0 else float('-inf')
            Aright = A[midA+1] if midA + 1 < lA else float('inf')
            Bleft = B[midB] if midB >= 0 else float('-inf')
            Bright = B[midB+1] if midB + 1 < lB else float('inf')
            # Check if partitioning is correct
            if Aleft <= Bright and Aright >= Bleft:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1