class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 if len(nums1) <= len(nums2) else nums2
        numb = nums1 if len(nums1) > len(nums2) else nums2
        m = len(nums)
        n = len(numb)

        start = 0
        end = m
        while end >= start:
            i = start + ((end - start) >> 1) #short list left long
            j = ((m + n + 1) >> 1) - i #big list left long
            
            if i == 0 or j == n:
                condition1 = True
            else :
                condition1 = nums[i-1] <= numb[j]
            if i == m or j == 0:
                condition2 = True
            else:
                condition2 = numb[j-1] <= nums[i]
                  
            if condition1 and condition2:
                if i == 0:
                    maxnums = numb[j-1]
                elif j == 0:
                    maxnums = nums[i-1]
                else:
                    maxnums = max(nums[i-1],numb[j-1])
                if (m+n) % 2:
                    return maxnums
                else:
                    if i == m:
                        minnumb = numb[j]
                    elif j == n:
                        minnumb = nums[i]
                    else:
                        minnumb = min(nums[i],numb[j])
                    return (maxnums + minnumb) / 2
            elif not condition1:
                end = i - 1
            else:
                start = i + 1
