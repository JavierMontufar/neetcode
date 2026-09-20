class Solution:
    def isValid(self, s: str) -> bool:
        parStack = []
        openBracket = "([{"
        closeBracket = ")]}"
        
        # Mapeo de apertura a cierre
        bracketMap = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in openBracket:
                parStack.append(c)
            elif c in closeBracket:
                if parStack and parStack[-1] == bracketMap[c]:
                    parStack.pop()  # Elimina el último elemento si es un par válido
                else:
                    return False  # Retorna False si no hay par o es incorrecto

        return not parStack # Si la pila está vacía, todos los paréntesis fueron válidos