class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        output = [1] * len(nums)
        while i < len(nums):
            mult = 1
            j = 0
            while j < len(nums):
                if(i != j):
                    mult *= nums[j]
                j += 1
            output[i] = mult
            i += 1
        return output