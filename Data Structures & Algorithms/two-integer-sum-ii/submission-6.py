class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) -1 #start empieza en 0 y end en len(numbers)-1

        while start < len(numbers) - 1: #recorremos start hasta que sea menos a len(numbers)-1
            while end > start: #mientras end sea 
                if numbers[start] + numbers[end] == target:
                    return [start+1, end+1]
                elif numbers[start] + numbers[end] > target:
                    end -= 1
                else:
                    start += 1
                
        