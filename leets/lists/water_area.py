class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0

        if len(height) <= 1:
            return 0

        for i1, j in enumerate(height):
            for i2, k in enumerate(height):
                small = min(j, k)
                diff = abs(i1 - i2)
                result = max(result, diff*small)

        return result
