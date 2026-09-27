import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, right = 0,0

        max_length = 0

        max_heap = [-nums[0]]
        min_heap = [nums[0]]

        while right <= len(nums)-1:
            # subarray = nums[left: right+1]
            # min_el = min(subarray)
            # max_el = max(subarray)
            # dif = abs(min_el-max_el)


            min_el = min_heap[0]
            max_el = -max_heap[0]
            dif = abs(min_el-max_el)

            if dif > limit:
                # heapq.heappop(min_heap, nums[left])
                min_heap.remove(nums[left])
                heapq.heapify(min_heap)
                max_heap.remove(-nums[left])
                heapq.heapify(max_heap)
                left += 1
            
            else:
                max_length = max(max_length, right-left+1)
                right += 1
                if right < len(nums):
                    heapq.heappush(min_heap, nums[right])
                    heapq.heappush(max_heap, -nums[right])
                
        
        return max_length