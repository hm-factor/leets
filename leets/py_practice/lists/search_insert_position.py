def searchInsert(self, nums: list[int], target: int) -> int:

    l, r = 0, len(nums)-1
    p = 0
    while l <= r:
        piv = l + (r-l)//2

        if target == nums[piv]:
            return piv
        elif target > nums[piv]:
            l = piv + 1
            p = piv
        elif target < nums[piv]:
            r = piv - 1
            p = piv

    return p + 1 if target > nums[p] else p
