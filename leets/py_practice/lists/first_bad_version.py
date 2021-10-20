# isBadVersion is an api that returns boolean for int

def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    l, r = 1, n
    while l < r:
        pivot = l + (r-l)//2
        if isBadVersion(pivot):
            r = pivot
        else:
            l = pivot+1
    return l
