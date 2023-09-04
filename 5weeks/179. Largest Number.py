import functools

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def comparator(s1, s2):
            if s1 + s2 < s2 + s1:
                return -1
            if s1 + s2 > s2 + s1:
                return 1
            
            return 0

        nums = [str(num) for num in nums]
        nums = sorted(nums, key=functools.cmp_to_key(comparator), reverse=True)

        return '0' if nums[0] == '0' else ''.join(nums)
