class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        answer = 0
        left, right = 0, len(height) - 1

        while left < right:
            answer = max(answer, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else: right -= 1

        return answer
