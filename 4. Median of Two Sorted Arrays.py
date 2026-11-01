class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)

        n = len(merged)

        # If the number of elements is odd
        if n % 2 == 1:
            return merged[n // 2]

        # If the number of elements is even
        return (merged[n // 2 - 1] + merged[n // 2]) / 2