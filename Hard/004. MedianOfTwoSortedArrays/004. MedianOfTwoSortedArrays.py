class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def merge(nums1, m, nums2, n):
            merged = [0] * (m+n)
            i = j = 0
            while(i < m and j < n):
                if(nums1[i] < nums2[j]):
                    merged[i+j] = nums1[i]
                    i += 1
                else:
                    merged[i+j] = nums2[j]
                    j += 1
            while(i < m):
                merged[i+j] = nums1[i]
                i += 1
            while(j < n):
                merged[i+j] = nums2[j]
                j += 1
            return merged
        merged = merge(nums1, len(nums1), nums2, len(nums2))
        k = len(merged) - 1
        if(k%2==1):
            return (merged[k//2] + merged[(k+2)//2])/2.0
        return merged[k//2]
        