class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack = []
        Operadores = "+-*/"
        for c in tokens:
            if c in Operadores:
                operador2 = int(Stack.pop())
                operador1 = int(Stack.pop())
                result = 0
                if c in "+":
                    result = operador1+operador2
                elif c in "-":
                    result = operador1-operador2
                elif c in "*":
                    result = operador1*operador2
                elif c in "/":
                    result = int(operador1/operador2)
                Stack.append(result)
            else:
                Stack.append(int(c))
        print(Stack)
        
        return Stack[-1]