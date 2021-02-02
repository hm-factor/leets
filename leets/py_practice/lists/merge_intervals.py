class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])
        # nlogn O(n)

        arr = []

        # linear O(n)
        for item in intervals:
            if not arr or arr[-1][1] < item[0]:
                arr.append(item)
            else:
                arr[-1][1] = max(arr[-1][1], item[1])

        return arr

        # arr = [None]
        # for a in intervals:
        #     last = arr[-1]
        #     low = a[0]
        #     high = a[1]
        #     if last == None:
        #         arr.pop()
        #         arr.append(a)
        #     elif last[1] >= low:
        #         #                 check if last el and curr el overlap
        #         low = min(low, last[0])
        #         high = max(high, last[1])
        #         arr.pop()
        #         arr.append([low, high])
        #     elif last[0] > low and last[1] > high:
        #         arr.append([low, high], -2)
        #     else:
        #         arr.append(a)
        # return arr
