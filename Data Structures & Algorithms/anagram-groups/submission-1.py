class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        used = [False] * len(strs)  # Para no repetir palabras ya agrupadas

        for i in range(len(strs)):
            if used[i]:
                continue

            anagram = [strs[i]]
            sortedWord = sorted(strs[i])
            used[i] = True

            for j in range(i + 1, len(strs)):
                if not used[j] and sortedWord == sorted(strs[j]):
                    anagram.append(strs[j])
                    used[j] = True

            anagrams.append(anagram)

        return anagrams 
        