class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        arr = [None]
        for a in intervals:
            last = arr[-1]
            low = a[0]
            high = a[1]
            if last == None:
                arr.pop()
                arr.append(a)
            elif last[1] >= low:
                #                 check if last el and curr el overlap
                low = min(low, last[0])
                high = max(high, last[1])
                arr.pop()
                arr.append([low, high])
            elif last[0] > low and last[1] > high:
                arr.append([low, high], -2)
            else:
                arr.append(a)
        return arr
