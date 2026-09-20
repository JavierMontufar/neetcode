class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frecDict = {}
        for num in nums:
            if num in frecDict:
                frecDict[num] += 1
            else:
                frecDict[num] = 1

        frecOrdenado = sorted(frecDict.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in frecOrdenado[:k]]
        

