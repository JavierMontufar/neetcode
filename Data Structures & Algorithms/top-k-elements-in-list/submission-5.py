class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frecDict = {}
        for num in nums:
            if num in frecDict:
                frecDict[num] += 1
            else:
                frecDict[num] = 1

        # Convierte esta lista en tuplas y ordena esa lista por el valor(frecuencia) es decir por el segundo elemento de cada tupla
        frecOrdenado = sorted(frecDict.items(), key=lambda item: item[1])

        print(frecOrdenado)  # [(num, frecuencia), ...]

        # Tomar los últimos k elementos y extraer las claves
        return [item[0] for item in frecOrdenado[-k:]]

