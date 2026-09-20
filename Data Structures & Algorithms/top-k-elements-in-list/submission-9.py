class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frecDict = {}
        for num in nums:
            if num in frecDict:
                frecDict[num] += 1
            else:
                frecDict[num] = 1

        arr = []
        for num, cnt in frecDict.items():
            arr.append([cnt, num])
        arr.sort()
        print(arr)
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

