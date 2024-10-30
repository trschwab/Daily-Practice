class Solution(object):
    # Brute force
    def twoSum_a(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # This version uses a hash table so we can keep runtime in O(n)
    def twoSum_b(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup_table = {}

        for index, element in enumerate(nums):
            complement = target - element

            if complement in lookup_table:
                return [index, lookup_table[complement]]
            else:
                lookup_table[element] = index