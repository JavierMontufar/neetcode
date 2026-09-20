class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dict = {}
        for num in nums:
            if num in Dict:
                Dict[num] += 1
            else:
                Dict[num] = 1

            if Dict[num] == 2:
                return True
        
        return False
        