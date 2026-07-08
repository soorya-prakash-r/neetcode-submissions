class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums2) - 1
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:
            mid = (l+r) // 2
            
            left_partition = half - mid - 2

            Aleft = nums1[left_partition] if left_partition >= 0 else float("-inf")
            Aright = nums1[left_partition+1] if left_partition+1 < len(nums1) else float("inf")
            Bleft = nums2[mid] if mid >= 0 else float("-inf")
            Bright = nums2[mid+1] if mid+1 < len(nums2) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total%2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 
                else:
                    return min(Aright, Bright)
            elif Bleft > Aright:
                r = mid - 1
            else:
                l = mid + 1

