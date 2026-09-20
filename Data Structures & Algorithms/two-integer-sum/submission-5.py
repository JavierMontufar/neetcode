class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}

        for i,num in enumerate(nums):
            difference = target-num
            if difference in Dict:
                index = Dict[difference]
                return[index, i]
                #TODO
            else:
                Dict[num]=i
        return []

        