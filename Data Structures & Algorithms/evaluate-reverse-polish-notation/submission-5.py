class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack = [] #Pila de numeros a los que se aplica el operador
        Operadores = "+-*/" #Operadores
        for c in tokens:
            if c in Operadores: #Si el caracter es un operador sacamos los dos ultimos elementos de la pila, calculamos el resultado y lo ponemos arriba de la pila
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
            else: #Si el carcater es un numero lo ponemos arriba de la pila
                Stack.append(int(c)) 
        print(Stack)
        
        return Stack[-1] #regresamos el tope de la pila