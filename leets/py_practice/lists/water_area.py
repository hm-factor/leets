class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ### SLIDING POINTERS ###

        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            small = min(height[left], height[right])
            area = max(area, small*(right - left))

            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1

        return area

        ### ENUMERATION ###

        # result = 0

        # if len(height) <= 1:
        #     return 0

        # for i1, j in enumerate(height):
        #     for i2, k in enumerate(height):
        #         small = min(j, k)
        #         diff = abs(i1 - i2)
        #         result = max(result, diff*small)

        # return result


