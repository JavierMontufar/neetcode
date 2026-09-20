class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict = {}

        for num in nums:
            if num in Dict:
                Dict[num] += 1
            else:
                Dict[num] = 1
        
        arr=[]

        for num, count in Dict.items():
            arr.append([count, num])
        
        arr.sort()
        res=[]

        while len(res)<k:
            res.append(arr.pop()[1])
        return res