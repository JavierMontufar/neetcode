class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxCount = 0

        for num in nums:
            if (num-1) not in nums: #Num es el comienzo de una secuencia
                count = 1
                while (num + count) in numsSet:
                    count += 1
                maxCount = max(count, maxCount)
        return maxCount

