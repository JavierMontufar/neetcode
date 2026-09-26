import heapq

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # montone_incr = sorted(nums)
        # monotone_dec = sorted(nums, reverse=True)

        # return (nums == montone_incr) or (nums == monotone_dec)

        increasing = True
        decreasing = True

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                increasing = False
            if nums[i] > nums[i-1]:
                decreasing = False
        
        return increasing or decreasing