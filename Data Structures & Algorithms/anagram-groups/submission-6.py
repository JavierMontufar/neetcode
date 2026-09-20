class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsDict = {}
        for s in strs:
            sortedWord = sorted(s) #Ordenamos la palabra
            sortedWord = "".join(sortedWord) #sorted te regresa un lista que tienes que convertirla a cadena
            if sortedWord in wordsDict: #Si esta la palabra en el diccionario
                wordsDict[sortedWord].append(s) #Le agregamos el valor s a la lista
            else:
                wordsDict[sortedWord] = [s] #Inicializamos una lista con el valor s
        
        print(wordsDict)
        return list(wordsDict.values())
        