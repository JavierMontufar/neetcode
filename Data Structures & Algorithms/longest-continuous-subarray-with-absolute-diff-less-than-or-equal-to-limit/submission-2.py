import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, right = 0,0

        max_length = 0

        max_heap = []
        min_heap = []

        while right <= len(nums)-1:
            subarray = nums[left: right+1]
            min_el = min(subarray)
            max_el = max(subarray)
            dif = abs(min_el-max_el)


            # min_el = min_heap[0]
            # max_el = max_heap[0]
            # dif = abs(min_el-max_el)

            if dif > limit:
                # heapq.heappop()

                left += 1
            
            else:
                max_length = max(max_length, len(subarray))
                right += 1
        
        return max_length