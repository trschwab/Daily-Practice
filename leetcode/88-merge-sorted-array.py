
# Pretty optimal
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        insert = len(nums1) - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[insert] = nums1[m - 1]
                m -=1
            else:
                nums1[insert] = nums2[n - 1]
                n -=1
            insert -= 1
        
        # In cases where nums1 is emptied first
        # We want to fill nums1 with remainder of nums2
        while n > 0:
            nums1[insert] = nums2[n - 1]
            insert -=1
            n -= 1

        return nums1
