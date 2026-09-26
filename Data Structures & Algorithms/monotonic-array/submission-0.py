import heapq

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        montone_incr = sorted(nums)
        monotone_dec = sorted(nums, reverse=True)

        return (nums == montone_incr) or (nums == monotone_dec)