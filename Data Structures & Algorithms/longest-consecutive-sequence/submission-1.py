class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxCount = 0

        for num in nums:
            if (num-1) not in nums: #Num es el comienzo de una secuencia
                count = 1 #como es el comienzo de una secuencia count es 1
                while (num + count) in numsSet: #Si num mas el cuena esta en el numsSet
                    count += 1 #Aumentamos la cuenta en 1
                maxCount = max(count, maxCount) #Regresamos la maxima entre count y maxCount
        return maxCount #regresamos maxcount

