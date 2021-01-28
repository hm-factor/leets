class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        min = 0
        result = 0

        if len(height) == 0 or len(height) == 1:
            return 0

        for idx, j in enumerate(height):
            idx1 = idx
            min = j
            for idx, k in enumerate(height):
                idx2 = idx
                if k < j:
                    min = k
                diff = abs(idx2 - idx1)
                if (diff*min) > result:
                    result = (diff*min)

        return result
