from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        basefreq = freq[k]
        max_gain = 0

        for v in freq:
            if v == k:
                continue

            current_sum = 0
            best_sum = 0

            for num in nums:
                if num == k:
                    score = -1
                
                elif num == v:
                    score = 1
                
                else:
                    score = 0
                
                current_sum = max(0, current_sum + score)
                best_sum = max(best_sum, current_sum)
            
            max_gain = max(max_gain, best_sum)
        
        return basefreq + max_gain
                