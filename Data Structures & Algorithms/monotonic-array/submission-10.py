import heapq

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # montone_incr = sorted(nums)
        # monotone_dec = sorted(nums, reverse=True)

        # return (nums == montone_incr) or (nums == monotone_dec)

        numbers = nums[:]

        numbers_max = nums[:]
        numbers_max = [-number for number in numbers_max]

        # max heap
        heapq.heapify(numbers_max)
        # min heap numbers
        heapq.heapify(numbers)

        increasing = True
        decreasing = True

        for index in range(len(nums)):
            min_el = heapq.heappop(numbers)
            max_el = -heapq.heappop(numbers_max)
            if nums[index] != min_el:
                increasing = False
            if nums[index] != max_el:
                decreasing = False
        
        return increasing or decreasing