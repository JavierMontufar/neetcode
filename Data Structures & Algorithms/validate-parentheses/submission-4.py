class Solution:
    def isValid(self, s: str) -> bool:
        parStack = []
        openBracket = "([{"
        
        # Mapeo de apertura a cierre
        bracketMap = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in openBracket:
                parStack.append(c)
            else:
                if parStack and parStack[-1] == bracketMap[c]: #Si la lista parStack no esta vacia y su ultimo elemento es igual al mapeo de "c"
                    parStack.pop()  # Elimina el último elemento si es un par válido
                else:
                    return False  # Retorna False si no hay par o es incorrecto

        return not parStack # Retorna true si la lista parStack esta vacia