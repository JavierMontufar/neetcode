class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = "([{"
        mapBrackets = {")":"(", "]":"[", "}":"{"}

        for caracter in s:
            if caracter in openBrackets:
                stack.append(caracter)
            
            else:
                if stack and stack[-1] == mapBrackets[caracter]:
                    stack.pop()
                else:
                    return False

        return not stack
