class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsDict = {}
        for s in strs:
            sortedWord = sorted(s)
            sortedWord = "".join(sortedWord)
            if sortedWord in wordsDict:
                wordsDict[sortedWord].append(s)
            else:
                wordsDict[sortedWord] = [s]
        
        print(wordsDict)
        return list(wordsDict.values())
        