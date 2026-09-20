class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Arreglo hash con los caracteres que han salido
        SetCaracteres = set()
        l = 0
        #res en 0
        res = 0
        
        #hacemos un for con r de 0 a la longitud de s
        for r in range(len(s)):
            caracter = s[r]
            #mientras el caracter este en el arreglo hash
            while caracter in SetCaracteres:
                #quitamos del arreglo hash el caracter s[l]
                SetCaracteres.remove(s[l])
                #aumentamos l a la derecha
                l += 1
            #agregamos al arreglo hash el caracter
            SetCaracteres.add(caracter)
            #obtenemos la longitud maxima entre resActual y la longitud de la substring
            res = max(res, r - l + 1)
        
        #regresamos la longitud de la substring
        return res