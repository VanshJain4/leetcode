from bisect import bisect_left, bisect_right
import math

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count_less_equal(x):
            count = 0
            for a in nums1:
                if a > 0:
                    count += bisect_right(nums2, x // a)
                elif a < 0:
                    # for negative a, b >= ceil(x / a)
                    count += len(nums2) - bisect_left(nums2, math.ceil(x / a))
                else:
                    if x >= 0:
                        count += len(nums2)
            return count
        
        # All possible min/max product values
        min_val = min(nums1[0] * nums2[0], nums1[0] * nums2[-1],
                      nums1[-1] * nums2[0], nums1[-1] * nums2[-1])
        max_val = max(nums1[0] * nums2[0], nums1[0] * nums2[-1],
                      nums1[-1] * nums2[0], nums1[-1] * nums2[-1])
        
        # Binary search on product values
        left, right = min_val, max_val
        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
