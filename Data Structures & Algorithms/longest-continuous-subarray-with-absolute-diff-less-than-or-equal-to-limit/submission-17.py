import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, right = 0,0

        max_length = 0

        max_heap = []
        min_heap = []

        while right <= len(nums)-1:

            heapq.heappush(min_heap, nums[right])
            heapq.heappush(max_heap, -nums[right])

            min_el = min_heap[0]
            max_el = -max_heap[0]

            while abs(min_el-max_el) > limit:
                min_heap.remove(nums[left])
                heapq.heapify(min_heap)
                max_heap.remove(-nums[left])
                heapq.heapify(max_heap)
                left += 1
                min_el = min_heap[0]
                max_el = -max_heap[0]
            
            max_length = max(max_length, right-left+1)
            right += 1
                
        
        return max_length