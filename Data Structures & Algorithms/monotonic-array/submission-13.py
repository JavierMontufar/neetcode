import heapq

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # montone_incr = sorted(nums)
        # monotone_dec = sorted(nums, reverse=True)

        # return (nums == montone_incr) or (nums == monotone_dec)

        numbers = nums[:]
        # min heap numbers
        heapq.heapify(numbers)
        value = True

        for index in range(len(nums)):
            min_el = heapq.heappop(numbers)
            if nums[index] != min_el:
                value = False
        

        numbers_max = nums[:]
        numbers_max = [-number for number in numbers_max]
        heapq.heapify(numbers_max)
        value2 = True

        for index in range(len(nums)):
            max_el = -heapq.heappop(numbers_max)
            if nums[index] != max_el:
                value2 = False
        
        return value or value2