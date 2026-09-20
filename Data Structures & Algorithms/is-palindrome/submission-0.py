class Solution:
    def isPalindrome(self, s: str) -> bool:
        cadena1 = ''.join(c for c in s if c.isalnum()).lower()
        cadena2 = cadena1[::-1]
        return cadena1 == cadena2