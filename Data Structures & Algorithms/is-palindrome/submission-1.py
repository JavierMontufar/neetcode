class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Limpiar y filtrar la cadena solo alfanuméricos, sin espacios
        cadena1 = ''.join(c for c in s if c.isalnum()).lower()
        #Invertir la cadena
        cadena2 = cadena1[::-1]
        #Comparar si son iguales
        return cadena1 == cadena2