class Solution:
    def isPalindrome(self, s: str) -> bool:
        cadena = ''.join(c for c in s if c.isalnum()).lower()
        cadena2 = cadena[::-1]
        return cadena == cadena2