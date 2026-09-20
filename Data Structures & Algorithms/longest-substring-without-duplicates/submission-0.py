class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        SetCaracteres = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            caracter = s[r]
            while caracter in SetCaracteres:
                SetCaracteres.remove(s[l])
                l += 1
            SetCaracteres.add(caracter)
            res = max(res, r - l + 1)
        
        return res